text = input()
while text:
    if len(text) == len(set(text)):
        print(text)
    text = input()