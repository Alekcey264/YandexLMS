from zipfile import ZipFile
import json


count = 0
with ZipFile("input.zip") as myzip:
    files = myzip.namelist()
    for file in files:
        if file[-5:] == ".json":
            with myzip.open(file, 'r') as myjson:
                data = myjson.read().decode('utf-8')
                data = json.loads(data)
                if data["city"] == "Москва":
                    count += 1
print(count)