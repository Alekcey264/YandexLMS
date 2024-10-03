count = int(input())
text = [input() for _ in range(count)]
count = int(input())
names = [input() for _ in range(count)]
for string in text:
    checker = True
    for item in names:
        if item in string:
            continue
        else:
            checker = False
            break
    if checker:
        print(string)