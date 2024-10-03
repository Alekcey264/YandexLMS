def groundhog_day(arr):
    for i in range(1, len(arr)):
        counter = [i]
        for j in range(len(arr[i])):
            if arr[i - 1][j] != arr[i][j]:
                counter.append(j)
        if len(counter) > 3:
            return tuple(counter)
    return (0, 0)
