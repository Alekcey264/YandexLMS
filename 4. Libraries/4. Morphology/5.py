import sys
import pymorphy3

#text = list(map(str.strip, sys.stdin))
text = "Тотчас же через лес побежали солдаты.\nСначала по двое и по трое, потом компаниями в десять и двадцать человек, и, наконец, такими толпами, что ими переполнился, казалось, весь лес.\nАлиса спряталась за дерево, чтобы ее не сбили с ног, и наблюдала за их движениями.\n— Кто это там опять в городе? — отважилась она спросить.\n— Как кто? Лев и Единорог, конечно, — ответил Король.\n— Дерутся из-за короны?\n— Ясное дело! — сказал Король. — И самое курьезное в этом деле, что это ведь моя корона. Побежим, посмотрим на них.\nОни побежали. Алиса, следуя за ними, повторяла слова старой песни:\nРаз за царскую корону бился Лев с Единорогом.\nОдолев, Единорога Лев гонял по всем дорогам.\nКто им хлеба дал, кто булки, кто дал пряника обоим,\nИ из города прогнали с барабанным громким боем.".split("\n")


morph = pymorphy3.MorphAnalyzer()
names = set()
anims = set()

for item in text:
    item = item.replace(',', ' ').replace('?', ' ').replace('!', ' ').replace('.', ' ').split()
    for word in item:
        if 'Name' in morph.parse(word)[0].tag:
            names.add(word)
            continue
        if 'anim' in morph.parse(word)[0].tag:
            anims.add(morph.parse(word)[0].inflect({'nomn', 'sing'}).word)
            continue

print(*sorted(list(names)))
print(*sorted(list(anims), key=lambda x: (len(x), x), reverse=True))
