sum_of_every = []


def refinement(arr):
    sum_of_every.extend(arr)
    avg = [0, 0]
    for item in sum_of_every:
        if item % 2 == sum(sum_of_every) % 2:
            avg[0] += item
            avg[1] += 1
    if avg[1] == 0:
        return 0
    else:
        return round(avg[0] / avg[1], 1)

print(refinement([1, 2, 3]))
print(refinement([4, 5, 6, 7]))
print(refinement([1]))