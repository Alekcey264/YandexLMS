from sys import stdin

text = ' '.join(list(map(str.strip, stdin)))
splitted = list()
temp_dict = dict()
last_step = 0
for i in range(2, len(text)):
    if (text[i - 1] == " " and text[i - 2] in ".?!") or i == len(text) - 1:
        splitted.append(text[last_step:i].strip())
        last_step = i
splitted[-1] += text[-1]
for item in splitted:
    for word in item[:-1].lower().split():
        if word not in temp_dict.keys():
            temp_dict[word] = ''
        temp_dict[word] += item[-1]
result = []
for key, value in temp_dict.items():
    if "!" not in value and "." in value and "?" in value:
        result.append(key)
print(*sorted(result), sep=" ")