def rests(num):
    return [item % num for item in lst]

lst = [42, 17, 34, 100501]
print(*rests(3))
print(*lst)