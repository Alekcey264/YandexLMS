gus = set()
for _ in range(int(input())):
    word = input()
    if word in gus:
        print("ДА")
    else:
        print("НЕТ")
    gus.add(word)
