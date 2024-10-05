from sys import stdin

counter = 0
types = {"далек", "далека", "далеку", "далека", "далеком", "далеке", "далеки", "далеков", "далекам", "далеков", "далеками", "далеках"}
for text in list(map(str.strip, stdin)):
    for word in text.split():
        if word.lower() in types:
            counter += 1
            break
print(counter)