goboi = set()
flute = set()
saksophone = set()

sets = [goboi, flute, saksophone]

for item in sets:
    word = input()
    while word:
        item.add(word)
        word = input()
    print(item)

print(sets[0] | sets[1])
print("krappa", sets[2] - (sets[0] | sets[1]))

# print(*(sets[0] ^ sets[1] ^ sets[2]), sep="\n")
