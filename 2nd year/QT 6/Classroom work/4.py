import csv

with open('vps.csv', 'r', encoding='utf-8') as f:
    reader = list(csv.reader(f, delimiter=';'))

value = float(input())
print(*[reader[i][0] for i in range(1, len(reader)) if float(reader[i][4]) >= value], sep="\n")