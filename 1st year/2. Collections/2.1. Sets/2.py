trafarets = set()
for _ in range(int(input())):
    number = set(input())
    trafarets |= number
print(len(trafarets))