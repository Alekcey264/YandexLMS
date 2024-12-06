import csv
from sys import stdin

with open('plantis.csv', 'w', encoding='utf-8') as f:
    writer = csv.writer(f, delimiter=';', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['nomen', 'definitio', 'pluma', 'Russian nomen', 'familia', 'Russian nomen familia'])
    text = list(map(str.strip, stdin))
    [writer.writerow(item.split('\t')) for item in text]
