def sorting_bis(key, reverse):
    if key == "abc":
        data.sort(reverse=reverse)
    elif key == "len":
        for i in range(len(data)):
            data[i] = (len(data[i]), data[i])
        print(data)
        if not reverse:
            for i in range(len(data)):
                for j in range(i, len(data)):
                    if data[i][0] > data[j][0]:
                        data[i], data[j] = data[j], data[i]
        else:
            for i in range(len(data)):
                for j in range(i, len(data)):
                    if data[i][0] < data[j][0]:
                        data[i], data[j] = data[j], data[i]
        for i in range(len(data)):
            data[i] = data[i][1]


data = ["one", "two", "three"]
sorting_bis("len", True)
print(data)