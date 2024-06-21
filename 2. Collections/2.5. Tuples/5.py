text = [input() for _ in range(int(input()))]
for i in range(len(text)):
    for j in range(1, len(text[i])):
        if text[i][j] < text[i][j - 1]:
            print((i, j))