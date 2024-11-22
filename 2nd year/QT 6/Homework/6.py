from sys import stdin

import csv

n, m = map(int, input().split())
results = list(map(str.split, map(str.strip, stdin)))
correct_values = list()
for line in results:
    if int(line[2]) >= m and int(line[3]) >= m and int(line[4]) >= m:
        temp_sum = int(line[2]) + int(line[3]) + int(line[4])
        if temp_sum >= n:
            correct_values.append(line + [temp_sum])
with open('exam.csv', 'w', encoding='utf-8') as f:
    writer = csv.writer(f, delimiter=';', quoting=csv.QUOTE_MINIMAL)
    if correct_values:
        writer.writerow(('Фамилия', 'имя', 'результат 1', 'результат 2', 'результат 3', 'сумма'))
        [writer.writerow(item) for item in correct_values]
