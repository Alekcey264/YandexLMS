from sys import stdin
import json


answers = list(map(str.strip, stdin))
points = 0
with open("scoring.json", "r", encoding="utf-8") as file:
    data = json.load(file)
for value1 in data.values():
    for item in value1:
        for num in item['required_tests']:
            if answers[num - 1] == "ok":
                points += (item['points'] / len(item['required_tests']))
print(int(points))