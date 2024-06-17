n = int(input())
matrix = dict()
for i in range(n):
    row = list(map(int, input().split()))
    num = n - i - 1
    elem = row[n - i - 1]
    if elem not in matrix.keys():
        matrix[elem] = row[:num - 1] + row[num + 1:]
    else:
        matrix[elem].extend(row[:num - 1] + row[num + 1:])
for key in matrix.keys():
    temp_value = list(set(matrix[key]))
    temp_value.sort(reverse=True)
    matrix[key] = temp_value
print(matrix)