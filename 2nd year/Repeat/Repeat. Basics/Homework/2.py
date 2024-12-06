points = list()
correct_points = list()
left = (1000000000000, 0)
right = (-100000000000000, 0)
top = (0, -10000000000000000)
bottom = (0, 10000000000000000)
for _ in range(int(input())):
    point = tuple(map(int, input().split()))
    points.append(point)
    if point[0] > 0 and abs(point[1]) < point[0]:
        correct_points.append(point)
    elif point[0] < 0 and abs(point[1]) < abs(point[0]):
        correct_points.append(point)
for point in points:
    if point[0] < left[0]:
        left = point
    if point[0] > right[0]:
        right = point
    if point[1] > top[1]:
        top = point
    if point[1] < bottom[1]:
        bottom = point
if correct_points:
    print(*correct_points, sep="\n")
print(f"left: {left}")
print(f"right: {right}")
print(f"top: {top}")
print(f"bottom: {bottom}")
