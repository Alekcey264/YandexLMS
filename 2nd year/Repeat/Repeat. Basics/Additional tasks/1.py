from sys import stdin


print(len([string for string in list(map(str.strip, stdin)) if "далек" in string.lower()]))
