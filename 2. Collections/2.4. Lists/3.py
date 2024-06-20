text = input()
words = list()
while text:
    words.append(text)
    text = input()
max_l = 0
for item in words:
    if len(item) > max_l:
        max_l = len(item)
for word in words[::-1]:
    if len(word) < max_l:
        while len(word) != max_l:
            word = word + "-"
            if len(word) == max_l:
                break
            else:
                word = "-" + word
    print(word)