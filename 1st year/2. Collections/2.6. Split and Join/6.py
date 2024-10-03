s, lenght, text = input().split(" ")
text = text.split(s)
print(*[item for item in text if len(set(item)) >= int(lenght)], sep=s[::-1])