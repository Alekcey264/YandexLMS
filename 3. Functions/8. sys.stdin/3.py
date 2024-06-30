#data = ['1; 2; 3; 7; 4', '3; 2; 1; 10; 1', '2; 0; 3; 1; 2; 2']

import sys

data = list(map(str.strip, sys.stdin))
counter = 0
for item in data:
    if not all(list(map(lambda x: x%5, list(map(int, item.split(";")))))):
        counter += 1
if counter >= len(data):
    print("FAIL")
else:
    print("OK")