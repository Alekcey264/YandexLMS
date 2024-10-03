birds = dict()
text = input()
while text:
    text = text.split(": ")
    birds[text[0]] = birds.get(text[0], 0) + int(text[1])
    text = input()
print(birds)