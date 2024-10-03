days = int(input())
info = list()
for _ in range(2):
    temp_dict = dict()
    for _ in range(days):
        text = input().split()
        temp_dict[text[0]] = temp_dict.get(text[0], 0) + int(text[1])
    info.append(temp_dict)
min_value = 1000000
for i in range(2):
    info[i] = sorted(list(info[i].items()), key=lambda x: x[0])
for i in range(days):
    temp_value = info[0][i][1] // info[1][i][1]
    if temp_value < min_value:
        min_value = temp_value
print(min_value)