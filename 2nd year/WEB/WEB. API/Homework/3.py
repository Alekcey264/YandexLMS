import requests
from conf import API_KEY

cities = input().split(", ")
cur_city = (None, None)
for i in range(len(cities)):
    city_url = f"http://geocode-maps.yandex.ru/1.x/?apikey={API_KEY}&geocode={cities[i]}&format=json"
    response = requests.get(city_url)
    if response:
        response_json = response.json()
        toponym = response_json["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["Point"]["pos"]
        if not cur_city[1] or cur_city[1] >= float(toponym.split()[1]):
            cur_city = (cities[i], float(toponym.split()[1]))
print(cur_city[0])