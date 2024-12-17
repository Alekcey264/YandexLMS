with open('prices.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

if lines:
    sum = 0
    for line in lines:
        line = line.split('\t')
        sum += (int(line[1]) * float(line[2]))
    print('{:.2f}'.format(sum))
else:
    print(0)
