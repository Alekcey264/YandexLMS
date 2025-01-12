import requests
from conf import API_KEY


task = ["Хабаровск", "Уфа", "Нижний Новгород", "Калининград"]
for item in task:
    request_url = f"https://geocode-maps.yandex.ru/1.x/?apikey={API_KEY}&geocode={item}&format=json"
    response = requests.get(request_url)
    if response:
        response_json = response.json()
        toponym = response_json["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
        toponym_oblast = toponym["metaDataProperty"]["GeocoderMetaData"]["Address"]["Components"][1]["name"]
        print(f"Город {item} находится в следующей области: {toponym_oblast}")