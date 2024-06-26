eras = {'Archaea': range(2800000, 45000000), 'Proterozic': range(635000, 2800000),
        'Paleozoic': range(300000, 635000), 'Mesozoic': range(145000, 300000),
        'Cenozoic': range(145000)}
num = input()
while num:
    for era, time in eras.items():
        if int(num) in time:
            print(era)
            break
    num = input()