buildings = list(map(int, input().split()))
accepted = list()
for i in range(len(buildings)):
    checker = True
    for item in buildings[:i]:
        if item >= buildings[i]:
            checker = False
            break
    if checker:
        accepted.append(buildings[i])
print(*accepted, sep=">>")