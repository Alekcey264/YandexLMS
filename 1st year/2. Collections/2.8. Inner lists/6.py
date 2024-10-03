count = int(input())
num = int(input())
plants = list()
for _ in range(num):
    plant = input()
    plants.append((len(plant), plant))
plants.sort()
for i in range(0, count):
    items = plants[i::count]
    temp_list = []
    for item in items:
        temp_list.append(item[1])
    print(*temp_list, sep=", ")
