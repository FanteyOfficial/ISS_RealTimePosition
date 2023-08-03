from urllib.request import urlopen
import json
from geopy.geocoders import Nominatim
import geopy.geocoders

from time import sleep

import certifi
import ssl

from datetime import datetime

ctx = ssl._create_unverified_context(cafile=certifi.where()) # mumble mumble mumble fa cose per far sì che l'autenticazione funzioni
geopy.geocoders.options.default_ssl_context = ctx

geolocator = Nominatim(scheme="https", user_agent="Test")

counter = 0

data = {}

filename = "ISS_Data.json"

print("Locating the ISS...")

while True:
    response = urlopen("http://api.open-notify.org/iss-now.json")
    obj = json.loads(response.read())

    # Assign Latitude & Longitude
    latitude = obj['iss_position']['latitude']
    longitude = obj['iss_position']['longitude']

    # print(f"Latitude: {latitude}\nLongitude: {longitude}")

    location = geolocator.geocode(f"{latitude},{longitude}", timeout=10) # daily limitis 86400 requests per day (1sec * 60 * 60 * 24)

    if location is None:
        location = "Location is somewhere on the water"

    """print("\nISS current position:")
    print(location)

    print("\n-----\n")"""

    data[f'data{counter}'] = {
        "datetime": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        "latitude": latitude,
        "longitude": longitude,
        "location": str(location)
    }

    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

    sleep(0.5)

    counter += 1
    #print(counter)
