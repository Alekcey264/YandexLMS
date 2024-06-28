def quarters(*arr):
    points = {"I": 0, "II": 0, "III": 0, "IV": 0}
    for point in arr:
        if point[0] > 0 and point[1] > 0:
            points["I"] += 1
        elif point[0] < 0 and point[1] > 0:
            points["II"] += 1
        elif point[0] < 0 and point[1] < 0:
            points["III"] += 1
        elif point[0] > 0 and point[1] < 0:
            points["IV"] += 1
    return points


data = [(-5, 1), (-1, 3), (2, -1), (0, 3)]
for k, v in sorted(quarters(*data).items()):
    print(f'{k}:\t{v}')