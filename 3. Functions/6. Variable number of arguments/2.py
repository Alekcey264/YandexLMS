def accumulation(*data):
    sum_of = [0]
    for item in data:
        sum_of.append(sum_of[-1] + item)
    return sum_of


data = [1, 2, 3, 4, 5]
print(*accumulation(*data))