import csv

with open('rez.csv', 'r', encoding='utf-8') as f:
    reader = list(csv.reader(f, delimiter=','))[1:]

school, num = input().split()
if len(school) == 1:
    school = '0' + school
if len(num) == 1:
    num = '0' + num
needed_value = list()
for item in reader:
    current_school = item[2].split('-')[2]
    current_num = item[2].split('-')[3]
    if current_school == school and num == current_num:
        needed_value.append((item[1].split()[3], item[-1]))

needed_value = sorted(sorted(needed_value, key=lambda x: x[0], reverse=True), key=lambda x: -int(x[1]))
for item in needed_value:
    print(*item)