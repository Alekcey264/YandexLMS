def function(*arr, func):
    return func(arr)

data = [1, 2, 15, 3]
f = max
print(function(*data, func=f))