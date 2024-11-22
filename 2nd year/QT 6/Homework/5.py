import csv

region = input()
first_year, second_year = input().split()

with open('salary.csv', 'r', encoding='utf-8') as f:
    reader = list(filter(lambda x: x['Федеральный округ'] == region, list(csv.DictReader(f, delimiter=';'))))

correct_values = list()
for item in reader:
    first_value = item[first_year]
    second_value = item[second_year]
    if int(second_value) / int(first_value) <= 1.04:
        correct_values.append((item['Субъект'], first_value, second_value))

with open('out_file.csv', 'w', encoding='utf-8') as f:
    writer = csv.writer(f, delimiter=';', quoting=csv.QUOTE_MINIMAL)
    if correct_values:
        writer.writerow(['Субъект', first_year, second_year])
        for row in correct_values:
            writer.writerow(row)
