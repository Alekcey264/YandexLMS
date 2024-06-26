claws = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8}


def horse(x, y):
    x = list(x)
    y = list(y)
    x_axis = abs(claws[x[0]] - claws[y[0]])
    y_axis = abs(int(x[1]) - int(y[1]))
    print((x_axis == 2 and y_axis == 1) or (x_axis == 1 and y_axis == 2))
