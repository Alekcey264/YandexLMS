import csv

with open('wares.csv', 'r', encoding='utf-8') as f:
    lines = csv.reader(f, delimiter=';')
    value = 1000
    lines = list(filter(lambda x: int(x[1]) <= value, list(lines)[1:]))
    lines = sorted(lines, key=lambda x: int(x[1]))
    for i in range(len(lines)):
        lines[i][1] = int(lines[i][1])

used_lines = dict()
if lines:
    while value >= lines[0][1]:
        used_lines[lines[0][0]] = used_lines.get(lines[0][0], 0) + 1
        if used_lines[lines[0][0]] >= 10:
            lines.pop(0)
        else:
            value -= lines[0][1]
    if used_lines:
        output = list()
        for key, value in used_lines.items():
            output.extend([key] * value)
        print(', '.join(output))
    else:
        print('error')
else:
    print('error')
