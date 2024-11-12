with open('Homework/input.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

if lines:
    files = dict()
    multipliers = {'B': 0, 'KB': 1, 'MB': 2, 'GB': 3, 'TB': 4}
    for line in lines:
        line = line.split()
        line[1] = int(line[1]) * (1024 ** multipliers[line[2]])
        ex = line[0][line[0].index('.') + 1:]
        if ex not in files.keys():
            files[ex] = list()
        files[ex].append(tuple(line[:-1]))
    for item in sorted(files.keys()):
        values = sorted(files[item], key=lambda x: x[0])
        sum_of = sum(list(map(lambda x: x[1], values)))
        index = 0
        while sum_of >= 1024:
            sum_of /= 1024
            index += 1
        index = [key for key, value in multipliers.items() if index == value][0]
        text = '\n'.join(list(map(lambda x: x[0], values)))
        with open('output.txt', 'a', encoding='utf-8') as f:
            f.write(text)
            f.write('\n----------\n')
            f.write('Summary: {:.0f} {} \n\n'.format(sum_of, index))