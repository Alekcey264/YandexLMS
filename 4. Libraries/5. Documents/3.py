import sys


text = list(map(str.rstrip, sys.stdin))
for item in text:
    print(item.count("\t"))