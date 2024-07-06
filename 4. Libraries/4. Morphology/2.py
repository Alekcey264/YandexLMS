import sys
import pymorphy3

text = "добрая дракона\nзлой волки\nкотята милый\nвесёлые собакой\nлес еловые\nглубокий обрывы\nглупые ухмылкам\nсеренькое небом\nрыбы красивое".split("\n")
#text = list(map(str.strip, sys.stdin))
morph = pymorphy3.MorphAnalyzer()


for i in range(len(text)):
    new_str = ''
    text[i] = text[i].split()
    res = morph.parse(text[i][0])[0]
    if 'ADJF' not in res.tag and 'ADJS' not in res.tag:
        text[i][0], text[i][1] = text[i][1], text[i][0]
    noun = set(str(morph.parse(text[i][1])[0].tag).replace(" ", ",").split(",")[1:])
    print(noun)
    text[i][0] = morph.parse(text[i][0])[0].inflect({'sing', 'anim', 'gent'}).word

print(text)
