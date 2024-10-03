text = input()
tale = list()
while text != "разбитое корыто":
    tale.append(text)
    text = input()
for i in range(len(tale)):
    for j in range(i + 1, len(tale)):
        if len(tale[i]) > len(tale[j]):
            tale[i], tale[j] = tale[j], tale[i]
print(*tale, sep="\n")