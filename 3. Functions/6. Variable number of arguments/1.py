def cat(first, last, *other):
    unique = set()
    temp_list = other[0]
    for item in temp_list:
        if item.lower() >= first.lower() and item.lower() <= last.lower():
            unique.add(item)
    return unique


text = input().split()
print(*cat(text[0], text[-1], text[1:-1]))