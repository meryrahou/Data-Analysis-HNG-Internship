import pandas as pd
from geopy.geocoders import OpenCage
from geopy.distance import geodesic
import numpy as np


# Loading crosschecked CSV into a DataFrame

# Initialize OpenCage geocoder with personal API key
geolocator = OpenCage(api_key='609fd728f00040729a345e1e86063f27')

# Example address to geocode
location = "KOFAR DOGO MAI KEMI II, DOGO NINI, POTISKUM, YOBE, Nigeria"
# Geocode the address
location = geolocator.geocode(location)

if location:
    print(location.latitude, location.longitude)
else:
    print("Location not found.")
