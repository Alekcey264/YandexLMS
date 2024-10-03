from sys import stdin

word = input()
word_letters = dict()
for letter in word:
    word_letters[letter] = word_letters.get(letter, 0) + 1
words = list(map(str.strip, stdin))
answer = list()
for item in words:
    item_letters = dict()
    for letter in item:
        item_letters[letter] = item_letters.get(letter, 0) + 1
    flag = True
    for key, value in item_letters.items():
        if key in word_letters.keys() and word_letters[key] and word_letters[key] >= value:
            continue
        else:
            flag = False
            break
    if flag:
        answer.append(item)
print(len(answer), *answer, sep="\n")