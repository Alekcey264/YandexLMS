import requests
import sys

from conf import GEOCODER_API_KEY, SEARCH_API_KEY


geocoder_api_server =  "https://geocode-maps.yandex.ru/1.x/"
search_api_server = "https://search-maps.yandex.ru/v1"

toponym_to_find = " ".join(sys.argv[1:])
search_params = {
    "apikey": SEARCH_API_KEY,
    "text": toponym_to_find,
    "lang": "ru_RU",
    "format": "json"
}
search_response = requests.get(search_api_server, params=search_params)

if not search_response:
    print("Bad request to Search")
    print(search_response.reason, search_response.content)
    sys.exit(1)

json_search_response = search_response.json()
main_toponym = json_search_response["features"][0]
main_toponym_coords = main_toponym["geometry"]["coordinates"]

geocoder_params = {
    "apikey": GEOCODER_API_KEY,
    "geocode": "{0},{1}".format(main_toponym_coords[0], main_toponym_coords[1]),
    "lang": "ru_RU",
    "kind": "district",
    "format": "json"
}
geocoder_response = requests.get(geocoder_api_server, params=geocoder_params)

if not geocoder_response:
    print("Bad request to Geocoder")
    print(geocoder_response.reason, geocoder_response.content)
    sys.exit(1)

json_geocoder_response = geocoder_response.json()
geocoder_toponym = json_geocoder_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
geocoder_toponym_district = geocoder_toponym["metaDataProperty"]["GeocoderMetaData"]["Address"]["Components"][-1]["name"]
print(geocoder_toponym_district)