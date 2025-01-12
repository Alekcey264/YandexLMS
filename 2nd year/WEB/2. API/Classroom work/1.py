import requests
from conf import API_KEY


geocoder_request = f"https://geocode-maps.yandex.ru/1.x/?apikey={API_KEY}&geocode=Красная+площадь+1+Москва&format=json"
response = requests.get(geocoder_request)
if response:
    json_response = response.json()
    toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
    toponym_address = toponym["metaDataProperty"]["GeocoderMetaData"]["Address"]['Components']
    toponym_coords = toponym["Point"]["pos"]
    print(", ".join([item["name"] for item in toponym_address]))
    print(toponym_coords)