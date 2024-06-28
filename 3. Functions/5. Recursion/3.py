def power(x, p):
    if p == 0:
        return 1
    elif p < 0:
        return 1 / power(x, -p)
    else:
        return x * power(x, p - 1)
    

print(power(2, 12))