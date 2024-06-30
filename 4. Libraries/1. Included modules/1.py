from math import log2

text = input()
print(len(text) * log2(len(set(text))))