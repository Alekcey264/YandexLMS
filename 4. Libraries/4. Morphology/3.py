import sys
import pymorphy3


text = "варкалось шорька пырялись 1\nвечерело 28 темнеющий зелюки пырялись\nмюмзик сладко хрюкотал 32\nи пылкает огнем 42".split("\n")
#text = list(map(str.strip, sys.stdin))
morph = pymorphy3.MorphAnalyzer()
for item in text:
    numb = None
    noun = None
    item = item.split()
    for word in item:
        if 'NOUN' in morph.parse(word)[0].tag:
            noun = word
            continue
        if 'NUMB' in morph.parse(word)[0].tag:
            numb = word
            continue
    print(numb, morph.parse(noun)[0].make_agree_with_number(int(numb)).inflect({'nomn'}).word)
