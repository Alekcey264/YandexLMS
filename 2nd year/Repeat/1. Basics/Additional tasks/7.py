positions = dict()
for _ in range(int(input())):
    text = input().split('\t')
    positions[text[0]] = int(text[1])
input()
order = input()
counter = 0
check = dict()
last_order = ''
while order != ".":
    if order:
        if not last_order:
            counter += 1
        order = order.split('\t')
        check[counter] = check.get(counter, 0) + (positions[order[0]] * int(order[1]))
    last_order, order = order, input()
check_sum = 0
for key, value in check.items():
    print(f"{key}) {value}")
    check_sum += value
print(f"Итого: {check_sum}")