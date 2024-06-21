num = int(input())
classes = list()
for _ in range(num):
    temp_list = list()
    for _ in range(11):
        temp_list.append(int(input()))
    classes.append(temp_list)
min_num = 1000000000
max_index = 0
max_num = -1
min_index = 0
for i in range(11):
    avg = 0
    counter = 0
    for j in range(len(classes)):
        if classes[j][i] != 0:
            avg += classes[j][i]
            counter += 1
    if counter != 0:
        avg /= counter
    else:
        continue
    if avg > max_num:
        max_num = avg
        max_index = i + 1
    elif avg < min_num:
        min_num = avg
        min_index = i + 1
print(min_index, max_index)