import pandas as pd
from geopy.geocoders import OpenCage
from geopy.distance import geodesic
import numpy as np


# Loading crosschecked CSV into a DataFrame
df = pd.read_csv('YOBE_crosschecked.csv')

# Initialize OpenCage geocoder with personal API key
geolocator = OpenCage(api_key='609fd728f00040729a345e1e86063f27')

# Step 0 : Geocode an address
def geocode_address(state, lga, ward, pu_name=None, pu_code=None):
    location = f"{ward}, {lga}, {state}, Nigeria"  
    if pu_name:
        location = f"{pu_name}, {location}"
    elif pu_code:
        location = f"PU {pu_code}, {location}"
        
    try:
        result = geolocator.geocode(location)
        if result:
            return result.latitude, result.longitude
        else:
            print(f"No result found for: {location}")
            return None, None
    except Exception as e:
        print(f"Error geocoding {location}: {e}")
        return None, None

# Step 1: Calculate Geodesic Distance Between Polling Units
def calculate_distances(df):
    distances = {}
    for i, row_i in df.iterrows():
        for j, row_j in df.iterrows():
            if i != j:
                key = frozenset([i, j])
                if key not in distances:
                    distances[key] = geodesic((row_i['Latitude'], row_i['Longitude']), (row_j['Latitude'], row_j['Longitude'])).kilometers
    return distances

# Step 2: Identify Neighbouring Polling Units
def find_neighbours(df, distances, radius=1):
    neighbours = {index: [] for index in df.index}
    for (i, j), distance in distances.items():
        if distance <= radius:
            neighbours[i].append(j)
            neighbours[j].append(i)
    return neighbours

# Step 3: Calculate Outlier Scores
def calculate_outlier_scores(df, neighbours):
    outlier_scores = pd.DataFrame(index=df.index, columns=df.columns[3:])  # Assuming first 3 columns are ID, Lat, Long
    for index, row in df.iterrows():
        for party in df.columns[3:]:
            party_votes = row[party]
            neighbour_votes = [df.at[n, party] for n in neighbours[index] if n in df.index]
            if neighbour_votes:
                average_neighbour_votes = np.mean(neighbour_votes)
                outlier_scores.at[index, party] = abs(party_votes - average_neighbour_votes)
            else:
                outlier_scores.at[index, party] = None
    return outlier_scores

# Step 4: Sort and Report
def sort_and_report(outlier_scores):
    sorted_scores = outlier_scores.fillna(0).sum(axis=1).sort_values(ascending=False)
    top_3_outliers = sorted_scores.head(3)
    return top_3_outliers


# Actual work

# Geocoding
latitudes = []
longitudes = []

for index, row in df.iterrows():
    state, lga, ward = row['State'], row['LGA'], row['Ward']
    pu_name, pu_code = row.get('PU-Name'), row.get('PU-Code')
    
    latitude, longitude = geocode_address(state, lga, ward, pu_name=pu_name, pu_code=pu_code)
    latitudes.append(latitude)
    longitudes.append(longitude)

# Adding latitude and longitude to the DataFrame
df['Latitude'] = latitudes
df['Longitude'] = longitudes

distances = calculate_distances(df)
neighbours = find_neighbours(df, distances)
outlier_scores = calculate_outlier_scores(df, neighbours)
top_3_outliers = sort_and_report(outlier_scores)

print("Top 3 Outliers:", top_3_outliers)


# Saving the updated DataFrame to a new CSV file
df.to_csv('geocoded_data.csv', index=False)

df_neighbours = pd.DataFrame.from_dict(neighbours, orient='index').transpose()
df_neighbours.to_csv('neighbours.csv', index=False)

outlier_scores.to_csv('outlier_scores.csv', index=False)