places = [(int(input()), float(input())) for _ in range(int(input()))]
for i in range(len(places)):
    for j in range(i + 1, len(places)):
        if places[i][0] > places[j][0]:
            places[i], places[j] = places[j], places[i]
        elif places[i][0] == places[j][0]:
            if places[i][1] > places[j][1]:
                places[i], places[j] = places[j], places[i]
print(*places, sep="\n")