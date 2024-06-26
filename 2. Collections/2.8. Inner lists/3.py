numbers = []
numbers.append(list(map(int, input().split())))
while len(numbers[-1]) != 1:
    temp_list = []
    for i in range(0, len(numbers[-1]), 2):
        if i == len(numbers[-1]) - 1:
            temp_list.append(numbers[-1][i] + 0)
        else:
            temp_list.append(numbers[-1][i] + numbers[-1][i + 1])
    numbers.append(temp_list)
for item in numbers[::-1]:
    print(*item)