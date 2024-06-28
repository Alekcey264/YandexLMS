def degree_indicator(n, base):
    if abs(n - 1) < 1e-9:
        return 0
    elif (n < base and base > 1) or (n > base and base < 1):
        return degree_indicator(n * base, base) - 1
    else:
        return 1 + degree_indicator(n / base, base)
    
print(degree_indicator(1 / 625, 5))