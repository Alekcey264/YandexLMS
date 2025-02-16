import csv
import sys


text = list(map(lambda x: x.split('; '), map(str.strip, sys.stdin)))
uniques = [[], []]
for i in range(len(text)):
    if text[i][0] not in uniques[0]:
        uniques[0].append(text[i][0])
        uniques[1].append(text.index(text[i]))
text = [text[i] + [str(len(text[i][1]) * (int(text[i][2]) // 2))] for i in range(len(text)) if i in uniques[1]]
with open('fairytale.csv', 'w', newline='', encoding='utf-8') as csv_f:
    writer = csv.writer(csv_f, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['no', 'creature', 'habitat', 'stealth', 'power'])
    for num, item in enumerate(text, 1):
        writer.writerow([num] + item)
