separator = input()
text = input().split()
for item in text:
    print(*list(item.upper()), sep=separator, end=" ")