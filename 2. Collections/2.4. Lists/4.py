count = int(input())
words = [input() for _ in range(count)]
item = input()
if item in words:
    index_word = words.index(item) + 1
else:
    for word in words:
        if word[0].lower() > item[0].lower():
            index_word = words.index(word) + 1
    else:
        index_word = len(words)
print(index_word)