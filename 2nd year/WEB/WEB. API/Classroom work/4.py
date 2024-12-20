import requests
from conf import API_KEY


request_url = f"https://geocode-maps.yandex.ru/1.x/?apikey={API_KEY}&geocode=Москва+петровка+38&format=json"
response = requests.get(request_url)
if response:
    json_response = response.json()
    toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["metaDataProperty"]
    toponym_info = toponym["GeocoderMetaData"]["AddressDetails"]["Country"]["AdministrativeArea"]["Locality"]
    toponym_index = toponym_info["Thoroughfare"]["Premise"]["PostalCode"]["PostalCodeNumber"]
    print(toponym_index)