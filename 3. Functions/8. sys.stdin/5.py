data = ['1 3 6', '2 2 10 70 50', '20 10 1']
import sys

#data = list(map(str.strip, sys.stdin))
for i in range(len(data)):
    item = list(map(lambda x: any not in list(map(int, list(x))), data[i].split()))
    data[i] = item.count(True) > item.count(False)
if data.count(True) > data.count(False):
    print("ALUMINUM CUCUMBERS")
else:
    print("EVERGREEN TOMATOES")    