import pandas as pd
from geopy.geocoders import OpenCage

# Load your CSV into a DataFrame
df = pd.read_csv('YOBE_crosschecked.csv')

# Initialize OpenCage geocoder
geolocator = OpenCage(api_key='609fd728f00040729a345e1e86063f27')

# Function to geocode an address
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

# Iterate through rows and geocode
latitudes = []
longitudes = []
for index, row in df.iterrows():
    state = row['State']
    lga = row['LGA']
    ward = row['Ward']
    pu_name = row.get('PU-Name')  
    pu_code = row.get('PU-Code')  
    
    latitude, longitude = geocode_address(state, lga, ward, pu_name=pu_name, pu_code=pu_code)
    print(f"Geocoded {state}, {lga}, {ward}, {pu_name}, {pu_code} to {latitude}, {longitude}")
    latitudes.append(latitude)
    longitudes.append(longitude)

# Add latitude and longitude to the DataFrame
df['Latitude'] = latitudes
df['Longitude'] = longitudes

# Save the updated DataFrame to a new CSV file
df.to_csv('geocoded_data.csv', index=False)
