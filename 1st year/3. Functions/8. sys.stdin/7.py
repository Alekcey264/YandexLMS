count = int(input())
data = list()
for _ in range(count):
    item = input().split(", ")
    data.append((item[0], float(item[2]), int(item[1])))
for item in sorted(data, key=lambda x: (-x[2], x[0], x[1])):
    print(f"{item[0]}: {item[1]}; {item[2]}")
