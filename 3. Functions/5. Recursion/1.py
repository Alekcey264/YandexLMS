def func(n):
    if n == 0:
        return 0
    elif n > 0 and n % 3 == 0:
        return func(n / 3) + 1
    elif n % 3:
        return 2 + func(n - 1)

print(func(10000))