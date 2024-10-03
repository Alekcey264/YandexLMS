def rounding(arr):
    sum_of_first = 0
    sum_of_second = 0
    for item in arr:
        sum_of_first += item // 1
        sum_of_second += item % 1
    return (int(sum_of_first), round(sum_of_second, 2))
