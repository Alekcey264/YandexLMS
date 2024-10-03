def defense(*points):
    max_x = 0
    min_x = 0
    max_y = 0
    min_y = 0
    for item in points:
        if item[0] > max_x:
            max_x = item[0]
        elif item[0] < min_x:
            min_x = item[0]
        if item[1] > max_y:
            max_y = item[1]
        elif item[1] < min_y:
            min_y = item[1]
    return [max_x - min_x, max_y - min_y]

points = [(-5, 1), (-1, 3), (2, -1), (0, 3)]
print(*defense(*points))
points = [(1, 1), (-1, 2), (-3, -1)]
print(*defense(*points))