import csv

with open('alpha_oriona.csv', 'r', encoding='utf-8') as f:
    reader = list(csv.reader(f, delimiter=';'))[1:]

best_combo = list()
curr_combo = [reader[0]]
for i in range(1, len(reader)):
    if int(reader[i][2]) <= int(curr_combo[-1][2]):
        curr_combo.append(reader[i])
        if len(curr_combo) > len(best_combo):
            best_combo = curr_combo[:]
    else:
        curr_combo = [reader[i]]
with open('result.txt', 'w', encoding='utf-8') as f:
    f.write(str(len(best_combo)) + '\n')
    f.write(best_combo[0][0] + ' ' + best_combo[0][1])