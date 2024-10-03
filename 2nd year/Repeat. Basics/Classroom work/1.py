first, second = input(), input()
if first == second:
    print("ничья")
elif (first == "камень" and second == "ножницы" or 
      first == "ножницы" and second == "бумага" or 
      first == "бумага" and second == "камень"):
    print("первый")
else:
    print("второй")