import requests

address = input()
port = input()
a = input()
b = input()
params = {
    "a": a,
    "b": b
}
url = f"{address}:{port}"
response = requests.get(url, params=params)
if not response:
    print(response.status_code, response.reason)
else:
    response_json = response.json()
    print(sorted(response_json["result"]))
    print(response_json["check"])