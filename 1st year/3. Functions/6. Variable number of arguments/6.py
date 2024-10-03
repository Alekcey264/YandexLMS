def opinions(*arr):
    unique = dict()
    for item in arr:
        for key, value in item.items():
            if key not in unique.keys():
                unique[key] = set()
            unique[key].add(value)
    return unique


data = [{'f': 1, 's': 2}, {'s': 2, 't': 3},
        {'s': 3, 'f': 5}, {'f': 4}, {}]
print(opinions(*data))