from sys import stdin

info = list(map(str.strip, stdin))
info = [info[i + 1] for i in range(len(info) - 1) if info[i + 1] != '' and info[i] != '']
cabs = dict()
for item in info:
    num = int(item[item.rfind(' ') + 1:])
    if num not in cabs.keys():
        cabs[num] = list()
    if item[:item.rfind(' ')] not in cabs[num]:
        cabs[num].append(item[:item.rfind(' ')])
for key, value in dict(sorted(cabs.items(), key=lambda x: x[0])).items():
    print(f'{key}: {", ".join(value)}')
