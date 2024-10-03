count = int(input())
words = [input() for _ in range(count)]
item = input()
if item in words:
    index_word = words.index(item) + 1
else:
    words.append(item)
    words.sort()
    index_word = words.index(item)
print(index_word)