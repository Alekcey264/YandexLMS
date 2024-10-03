from math import prod


def multiplier(*data, key):
    args = list(filter(key, data))
    if args:
        return prod(args)
    else:
        return None

print(multiplier(2, 3, 4, 5, key=lambda x: x % 2))