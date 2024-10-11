emails = [input()[:-12] for _ in range(int(input()))]
names = [input() for _ in range(int(input()))]
for i in range(len(emails)):
    for j in range(len(emails[i]) - 1, -1, -1):
        if not emails[i][j].isdigit():
            emails[i] = emails[i][:j + 1]
            break
already_created = dict()
for item in emails:
    already_created[item] = already_created.get(item, 0) + 1
for name in names:
    if name not in already_created.keys():
        already_created[name] = 1
        print(f"{name}@untitled.py")
    else:
        print(f"{name + str(already_created[name])}@untitled.py")
        already_created[name] += 1