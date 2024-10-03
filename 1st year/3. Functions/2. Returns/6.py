'''def gears(arr, n, m):
    for item in arr:
        first = None
        second = None
        for num in item:
            if not num % n:
                first = num
                continue
            if not num % m:
                if second:
                    if second < num:
                        continue
                second = num
                continue
        if first and second:
            return (first, second)
    return (None, None)
'''

def gears(arr, n, m):
    temp_arr = list()
    first, second = None, None
    for item in arr:
        temp_arr.extend(item)
    for i in range(len(temp_arr)):
        for j in range(i, len(temp_arr)):
            if temp_arr[i] == 0:
                continue
            elif temp_arr[i] / temp_arr[j] == n / m:
                first = temp_arr[i]
                second = temp_arr[j]
            elif temp_arr[j] / temp_arr[i] == n / m:
                first = temp_arr[j]
                second = temp_arr[i]
    return (first, second)


data = [[0, 2, 30, 15], [14, 3, 21, 60], [7, 16, 4, 8]]
print(gears(data, 30, 7))