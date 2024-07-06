import pymorphy3
import sys


#text = list(map(str.strip, sys.stdin))
text = "Плывет, плывет кораблик\nНа запад, на восток.\nКанаты — паутинки,\nА парус — лепесток.\n\nСоломенные весла\nУ маленьких гребцов.\nВезет, везет кораблик\nПолфунта леденцов.\n\nВедет кораблик утка,\nИспытанный моряк.\n— Земля! — сказала утка. —\nПричаливайте! Кряк!".split("\n")
morph = pymorphy3.MorphAnalyzer()
nouns = {}
for item in text:
    item = item.replace(',', ' ').replace('?', ' ').replace('!', ' ').replace('.', ' ').split(" ")
    
