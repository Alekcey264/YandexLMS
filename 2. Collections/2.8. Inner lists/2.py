num = int(input())
matrix = list()
summer = 0
for i in range(num):
    row = list(map(int, input().split(", ")))
    row[i], row[-i - 1] = row[-i - 1], row[i]
    summer += (row[i] + row[-i - 1])
    matrix.append(row)
for item in matrix:
    print(*item)
print(summer)