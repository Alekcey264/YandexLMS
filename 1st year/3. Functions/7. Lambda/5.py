new = list()
for i in list(map(lambda y: y.split()[-1], filter(lambda x: len(x.split()) > 1, input().split("; ")))):
    if i[-3:] != "ino":
        new.append(i[:-2] + "ino")
    elif i[-3:] == "ino":
        new.append(i[:-3] + "lone")
print(*new, sep=", ")