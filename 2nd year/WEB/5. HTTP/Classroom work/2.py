import requests
import sys

from conf import STATIC_API_KEY, GEOCODER_API_KEY
from io import BytesIO
from PIL import Image
from toponym_help import get_spn


geocoder_api_server =  "https://geocode-maps.yandex.ru/1.x/"
static_api_server = "https://static-maps.yandex.ru/v1"

toponym_to_find = " ".join(sys.argv[1:])
geocoder_params = {
    "apikey": GEOCODER_API_KEY,
    "geocode": toponym_to_find,
    "format": "json"
}
geocoder_response = requests.get(geocoder_api_server, geocoder_params)

if not geocoder_response:
    print("Bad request to Geocoder")
    print(geocoder_response.reason, geocoder_response.content)
    sys.exit(1)

json_geocoder_response = geocoder_response.json()
toponym = json_geocoder_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
toponym_coords = toponym["Point"]["pos"]
toponym_x, toponym_y =  toponym_coords.split(" ")
static_params = {
    "ll": ",".join([toponym_x, toponym_y]),
    "spn": get_spn(json_geocoder_response),
    "maptype": "map",
    "apikey": STATIC_API_KEY,
    "pt": f'{",".join([toponym_x, toponym_y])},round',
}
static_repsonse = requests.get(static_api_server, params=static_params)

if not static_repsonse:
    print("Bad request to StaticAPI")
    print(static_repsonse.reason, static_repsonse.content)
    sys.exit(1)

Image.open(BytesIO(static_repsonse.content)).show()
