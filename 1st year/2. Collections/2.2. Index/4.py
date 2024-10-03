alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = int(input()) - 1
for i in range(4):
    print(alphabet[(number + i) % 26], end="")