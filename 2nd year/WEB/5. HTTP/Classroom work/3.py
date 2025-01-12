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
organization = json_search_response["features"][0]
org_name = organization["properties"]["CompanyMetaData"]["name"]
org_address = organization["properties"]["CompanyMetaData"]["address"]
org_hours = organization["properties"]["CompanyMetaData"]["Hours"]["Availabilities"]
if "TwentyFourHours" in org_hours[0].keys():
    org_hours = "Работает круглосуточно"
else:
    org_hours = org_hours[0]["Intervals"][0]
    org_hours = "Работает с {0} до {1}".format(org_hours["from"][:-3], org_hours["to"][:-3])
org_point = organization["geometry"]["coordinates"]
org_coords = "{0},{1}".format(org_point[0], org_point[1])

static_params = {
    "maptype": "map",
    "apikey": STATIC_API_KEY,
    "pt": '{0},round~{1},pm2dgl'.format(main_toponym_coords, org_coords),
}
static_repsonse = requests.get(static_api_server, params=static_params)

if not static_repsonse:
    print("Bad request to StaticAPI")
    print(static_repsonse.reason, static_repsonse.content)
    sys.exit(1)

Image.open(BytesIO(static_repsonse.content)).show()
print(org_address, org_name, org_hours, sep=", ")