data = ['трехмачтовое судно «Британия»... Глазго... потерпело   крушение... гони... южн... берег... два матроса...', 'капитан Гр... добрат... контин... пл... жесток... инд...', 'брошен этот  документ ... долготы и 37° 11`  широты... окажите им помощь... погибнут...']

import sys

#data = list(map(str.strip, sys.stdin))
for item in data:
    print(*list(filter(lambda x: x[-3:] != "...", item.split())), sep="; ")