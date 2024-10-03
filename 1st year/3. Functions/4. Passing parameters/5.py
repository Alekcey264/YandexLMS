def allocation(arr):
    tickets = list()
    for item in arr:
        if places[item[0] - 1][item[1] - 1] == 0:
            places[item[0] - 1][item[1] - 1] = 1
        else:
            tickets.append(item)
    return tickets

places = [[1, 1, 0, 0], [0, 0, 0, 1], [0, 1, 1, 0, 0, 0]]
data = [(2, 3), (1, 4), (3, 1), (2, 3), (3, 3)]
print(allocation(data))