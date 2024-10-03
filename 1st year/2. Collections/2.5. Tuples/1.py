num = int(input())
paths = list()
while num != 0:
    paths.append(num)
    num = int(input())
for i in range(len(paths)):
    for j in range(i + 1, len(paths)):
        if paths[i] > paths[j]:
            paths[i], paths[j] = paths[j], paths[i]
print(*paths[::-1], sep="->")
