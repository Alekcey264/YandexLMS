text = input().split()
lenght = [len(item) for item in text]
print(*list(map(lambda x: '*'*(max(lenght) - (len(x))) + x, text)), sep="\n")