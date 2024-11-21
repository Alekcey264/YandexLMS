import csv 

with open('wares1.csv', 'r', encoding='utf-8') as f:
    reader = list(csv.reader(f, delimiter=';', quotechar='"'))

print(*[item[0] for item in reader[1:] if int(item[1]) > int(item[2])], sep='\n')