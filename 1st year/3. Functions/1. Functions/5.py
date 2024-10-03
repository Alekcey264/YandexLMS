def template(a, b, c):
    if (a + b - c > 0) and (a + c - b > 0) and (b + c - a > 0):
        p = a + b + c
        p2 = p / 2
        print(f"Периметр: {p}")
        print(f"Площадь: {(p2 * (p2 - a) * (p2 - b) * (p2 - c)) ** 0.5}")
        if a == b  or b == c or a == c:
            print("Равнобедренный: да")
        else:
            print("Равнобедренный: нет")
        if a == b and a == c:
            print("Равносторонний: да")
        else:
            print("Равносторонний: нет")  
    else:
        print("None")


template(5, 4, 5)
template(2, 1, 3)