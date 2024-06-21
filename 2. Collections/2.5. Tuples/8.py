text = input()
text_new = str()
letters = set()
lang_en = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz "
lang_ru = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя "

for i in range(len(text)):
    if text[i] in lang_en or text[i] in lang_ru:
        text_new += text[i]

for letter in text_new:
    index = -1
    if letter == " ":
        continue
    elif letter in lang_en:
        for i in range(len(lang_en)):
            if letter == lang_en[i]:
                letters.add((letter, i + 1))
                break
    else:
        for i in range(len(lang_ru)):
            if letter == lang_ru[i]:
                letters.add((letter, i + 1))
                break

print(*letters, sep="\n")