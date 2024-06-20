text = input()
num = int(input())
checker = num
while num < len(text):
    checker = -checker
    if checker < 0:
        print(text[checker:])
        text = text[:checker]
    else:
        print(text[:checker])
        text = text[checker:]
print(text)