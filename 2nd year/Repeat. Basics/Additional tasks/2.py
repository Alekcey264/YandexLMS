from sys import stdin


counter = 0
for text in list(map(str.strip, stdin)):
    for word in text.split():
        if word.lower().startswith("далек"):
            counter += 1
            break
print(counter)