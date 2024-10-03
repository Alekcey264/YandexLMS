word = input()
text = list()
while word:
    text.append(word)
    word = input()
text_lens = list(text)
for i in range(len(text_lens)):
    for j in range(i + 1, len(text_lens)):
        if len(text_lens[i]) > len(text_lens[j]):
            text_lens[i], text_lens[j] = text_lens[j], text_lens[i]
for i in range(len(text)):
    for j in range(i + 1, len(text)):
        if text[i] > text[j]:
            text[i], text[j] = text[j], text[i]
if text == text_lens:
    print("YES")
else:
    for i in range(len(text)):
        if text[i] != text_lens[i]:
            print(text[i], text_lens[i])
            break