from urllib.request import urlopen
import json
from geopy.geocoders import Nominatim
import geopy.geocoders

import certifi
import ssl

response = urlopen("http://api.open-notify.org/iss-now.json")
obj = json.loads(response.read())

# print(obj['timestamp'])
print(obj['iss_position']['latitude'], obj['iss_position']['longitude'])

# Initialize Nominatim API

ctx = ssl._create_unverified_context(cafile=certifi.where())
geopy.geocoders.options.default_ssl_context = ctx

geolocator = Nominatim(scheme="https", user_agent="Test")

# Assign Latitude & Longitude
Latitude = obj['iss_position']['latitude']
Longitude = obj['iss_position']['longitude']

# Displaying Latitude and Longitude
print("Latitude: ", Latitude)
print("Longitude: ", Longitude)

# Get location with geocode
location = geolocator.geocode(Latitude + "," + Longitude)

if location is None:
    location = "Location is somewhere on the water"

# Display location
print("\nLocation of the given Latitude and Longitude:")
print(location)