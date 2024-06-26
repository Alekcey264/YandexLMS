words = [""] + input().split()
max_len = 0
for item in words:
    if len(item) > max_len:
        max_len = len(item)
print()
for i in range(max_len):
    for item in words:
        if i == 0:
            if item == "":
                print("_", end="")
            else:
                print(item[i], end="_")
        elif item == "":
            print("", end=" ")
        elif i >= len(item):
            print(" ", end=" ")
        else:
            print(item[i], end=" ")
    print("")
print()
for i in range(max_len - 1, -1, -1):
    for item in words:
        if i == 0:
            if item == "":
                print("_", end="")
            else:
                print(item[i], end="_")
        elif item == "":
            print("", end=" ")
        elif i >= len(item):
            print(" ", end=" ")
        else:
            print(item[i], end=" ")
    print("")