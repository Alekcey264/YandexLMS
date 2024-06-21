word = input()
print(*[letter for letter in input().split() if word in letter], sep=" ")
