import sys
import pymorphy3


text = list(map(str.strip, sys.stdin))
morph = pymorphy3.MorphAnalyzer()
for item in text:
    numb = None
    noun = None
    item = item.split()
    for word in item:
        if 'NOUN' in morph.parse(word)[0].tag:
            noun = morph.parse(word)[0]
            continue
        if 'NUMB' in morph.parse(word)[0].tag:
            numb = int(morph.parse(word)[0].word)
            continue
    print(numb, noun.make_agree_with_number(numb).inflect({'nomn'}).word)
