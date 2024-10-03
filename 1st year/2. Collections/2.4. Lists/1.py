num = int(input())
text = list()
for _ in range(num):
    text.append(input())
num = int(input())
names = list()
for _ in range(num):
    names.append(input())
for name in names:
    for i in range(len(text)):
        if name in text[i]:
            print(i + 1)
            break
    else:
        print("-1")
