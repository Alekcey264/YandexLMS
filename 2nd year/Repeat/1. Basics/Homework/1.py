first, second = input(), input()
if first == second:
    print("ничья")
elif first == "ножницы":
    if second == "пират" or second == "камень":
        print("второй")
    else:
        print("первый")
elif first == "бумага":
    if second == "ножницы" or second == "ром":
        print("второй")
    else:
        print("первый")
elif first == "камень":
    if second == "пират" or second == "бумага":
        print("второй")
    else:
        print("первый")
elif first == "ром":
    if second == "камень" or second == "ножницы":
        print("второй")
    else:
        print("первый")
else:
    if second == "ром" or second == "бумага":
        print("второй")
    else:
        print("первый")