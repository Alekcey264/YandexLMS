text = input()
messages = list()
while text:
    messages.append(text)
    text = input()
name = input()
correct = list()
for item in messages:
    if item.startswith("@" + name):
        correct.append(item[len("@" + name) + 1:].capitalize())
print(*sorted(correct), sep="\n")