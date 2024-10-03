text = [input() for _ in range(int(input()))]
for i in range(len(text) - 1):
    if text[i][-1] < text[i + 1][-1]:
        print((i + 1, text[i][:-2]))
