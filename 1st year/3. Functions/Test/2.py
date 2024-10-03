def creaks_and_groans(n, arr):
    temp_list = list()
    for i in range(len(arr)):
        if i % n:
            temp_list.append(arr[i])
    print(*temp_list, sep="")

list_ = ['скрип',
 'Какое счастье! ',
 'скрип', 'Я стоял, ',
 'скрип',
 'замахнувшись этим топором, ',
 'скрип', 'с тех пор, ',
 'скрип',
 'как заржавел.']
n = 2
creaks_and_groans(n, list_)