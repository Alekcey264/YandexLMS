import requests
import sys

from conf import STATIC_API_KEY, GEOCODER_API_KEY, SEARCH_API_KEY
from io import BytesIO
from PIL import Image


geocoder_api_server =  "https://geocode-maps.yandex.ru/1.x/"
static_api_server = "https://static-maps.yandex.ru/v1"
search_api_server = "https://search-maps.yandex.ru/v1"

toponym_to_find = " ".join(sys.argv[1:])
geocoder_params = {
    "apikey": GEOCODER_API_KEY,
    "geocode": toponym_to_find,
    "format": "json"
}
geocoder_response = requests.get(geocoder_api_server, params=geocoder_params)

if not geocoder_response:
    print("Bad request to Geocoder")
    print(geocoder_response.reason, geocoder_response.content)
    sys.exit(1)

json_geocoder_response = geocoder_response.json()
main_toponym = json_geocoder_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
main_toponym_coords = ",".join(main_toponym["Point"]["pos"].split(" "))
search_params ={
    "apikey": SEARCH_API_KEY,
    "text": "аптека",
    "lang": "ru_RU",
    "ll": main_toponym_coords,
    "type": "biz"
}
search_response = requests.get(search_api_server, params=search_params)

if not search_response:
    print("Bad request to Search")
    print(search_response.reason, search_response.content)
    sys.exit(1)

json_search_response = search_response.json()
orgs = json_search_response["features"]
points = f"{main_toponym_coords},round"
times = {
    0: "pm2gnm",
    1: "pm2blm",
    2: "pm2grm"
}

for item in orgs:
    item_coords = "{0},{1}".format(item["geometry"]["coordinates"][0], item["geometry"]["coordinates"][1])
    item_hours = item["properties"]["CompanyMetaData"]["Hours"]["Availabilities"][0]
    if "TwentyFourHours" in item_hours.keys():
        text = times[0]
    elif "Intervals" in item_hours.keys():
        text = times[1]
    else:
        text = times[2]
    points = points + "~" + item_coords + "," + text

static_params = {
    "maptype": "map",
    "apikey": STATIC_API_KEY,
    "pt": points,
}
static_repsonse = requests.get(static_api_server, params=static_params)

if not static_repsonse:
    print("Bad request to StaticAPI")
    print(static_repsonse.reason, static_repsonse.content)
    sys.exit(1)

Image.open(BytesIO(static_repsonse.content)).show()