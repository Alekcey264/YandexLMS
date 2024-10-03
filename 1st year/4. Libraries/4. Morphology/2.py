import sys
import pymorphy3


text = list(map(str.strip, sys.stdin))
morph = pymorphy3.MorphAnalyzer()
for i in range(len(text)):
    new_str = ''
    text[i] = text[i].split()
    res = morph.parse(text[i][0])[0]
    if 'ADJF' not in res.tag and 'ADJS' not in res.tag:
        text[i][0], text[i][1] = text[i][1], text[i][0]
    noun = set(str(morph.parse(text[i][1])[0].tag).replace(" ", ",").split(",")[2:])
    if 'plur' in noun:
        noun.discard('masc')
        noun.discard('femn')
        noun.discard('neut')
        noun.discard('ms-f')
        noun.discard('GNdr')
    noun.discard('Inmx')
    noun.discard('Sgtm')
    noun.discard('Pltm')
    noun.discard('Fixd')
    print(noun)
    text[i][0] = morph.parse(text[i][0])[0].inflect(noun).word
[print(*item, sep=" ") for item in text]
