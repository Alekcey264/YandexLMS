order = input().split(" -> ")
names = list()
for _ in range(int(input())):
    names.append(input())
for name in names:
    num = order.index(name)
    if num == 0:
        print(" -> ".join(order[:2]))
    elif num == len(order) - 1:
        print(" -> ".join(order[-2:]))
    else:
        print(" -> ".join(order[num - 1:num + 2]))
