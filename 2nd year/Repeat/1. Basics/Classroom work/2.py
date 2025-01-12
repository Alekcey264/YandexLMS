points = list()
parts = {"I": 0, "II": 0, "III": 0, "IV": 0}
for _ in range(int(input())):
    x, y = tuple(map(int, input().split()))
    if x == 0 or y == 0:
        points.append((x, y))
    else:
        if x > 0 and y > 0:
            parts["I"] += 1
        elif x < 0 and y > 0:
            parts["II"] += 1 
        elif x < 0 and y < 0:
            parts["III"] += 1
        else:
            parts["IV"] += 1
if points:
    print(*points, sep="\n")
for key, value in parts.items():
    print(f"{key}: {value}", end="")
    if key != "IV":
        print(", ", end="")
    else:
        print(".")