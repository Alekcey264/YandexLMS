count = int(input())
word = ""
for i in range(count):
    text = input()
    if i >= len(text):
        word = "None"
        break
    else:
        word += text[-(i + 1)]
print(word)