text = input()
index = 0
for i in range(len(text)):
    if text[i] == "-":
        index = i
print(text[index + 1:], "-", text[:index], sep="")