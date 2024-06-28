text = input().split()
print(*[word for word in filter(lambda x: len(set(x.lower()) & set(text[1].lower())) >= 6, text)], sep=",")
