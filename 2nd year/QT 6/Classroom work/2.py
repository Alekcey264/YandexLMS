import csv

with open('wares.csv', 'r', encoding='utf-8') as f:
    lines = csv.reader(f, delimiter=';')
    value = 1000
    lines = list(filter(lambda x: int(x[1]) <= value, list(lines)[1:]))
    lines = sorted(lines, key=lambda x: -int(x[1]))

used_lines = dict()
