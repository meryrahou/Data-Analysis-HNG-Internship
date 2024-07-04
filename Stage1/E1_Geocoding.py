import pandas as pd
from geopy.geocoders import OpenCage


# Loading crosschecked CSV into a DataFrame
df = pd.read_csv('./Stage1/YOBE_crosschecked.csv')

# Initialize OpenCage geocoder with personal API key
geolocator = OpenCage(api_key='609fd728f00040729a345e1e86063f27')

# Step 0 : Geocode an address
def geocode_address(state, lga, ward, pu_name=None, pu_code=None):
    location = f"{ward}, {lga}, {state}, Nigeria"  
        
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


# Geocoding
latitudes = []
longitudes = []
n = 1
for index, row in df.iterrows():
    state, lga, ward = row['State'], row['LGA'], row['Ward']
    pu_name, pu_code = row.get('PU-Name'), row.get('PU-Code')
    
    latitude, longitude = geocode_address(state, lga, ward, pu_name=pu_name, pu_code=pu_code)
    print(f"{n} of {len(df)}: {latitude}, {longitude}")
    n += 1
    latitudes.append(latitude)
    longitudes.append(longitude)

# Adding latitude and longitude to the DataFrame
df['Latitude'] = latitudes
df['Longitude'] = longitudes



# Saving the updated DataFrame to a new CSV file
df.to_csv('./Stage1/geocoded_data.csv', index=False)
