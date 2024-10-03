def graph(func):
    print('x', end="\t")
    x_axis = list(range(-10, 11))
    print(*x_axis, sep='\t')
    print('y', end='\t')
    y_axis = list()
    for x in x_axis:
        y_axis.append(eval(func.replace('x', f"({str(x)})")))
    print(*y_axis, sep='\t')
