string = input()
text = list()
while string:
    text.append(string)
    string = input()
start = int(input()) - 1
finish = int(input()) - 1
max_l = str()
for item in text[start:finish + 1]:
    if len(item) > len(max_l):
        max_l = item
print(max_l)