def tunnel(arr):
    if len(arr) == 1:
        return arr[0]
    elif len(arr) == 2:
        return arr[0] + arr[1]
    else:
        return tunnel(arr[1:-1])
    
rock = [1, 2, 3, 4, 1]
print(tunnel(rock))