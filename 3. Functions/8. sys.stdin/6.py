data = ['Расстояние до Луны в среднем 384000 км.', 'До Плутона со скоростью 8000 км/с лететь около 750000 с.', 'Марсианские сутки длятся 24 часа 37 минут.', 'Земная ось наклонена под углом 23 градуса.']

import sys

#data = list(map(str.strip, sys.stdin))
sorted_data = list()
for item in data:
    if any(letter.isdigit() for letter in item):
        item = list(map(int, filter(lambda x: x.isnumeric(), item.split())))
        sorted_data.append((len(item), sum(item)))
if not sorted_data:
    print('-1')
else:
    print(sorted(sorted_data, key=lambda x: (-x[0], x[1]))[0][1])