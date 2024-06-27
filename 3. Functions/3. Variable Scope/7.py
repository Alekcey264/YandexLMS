menu = dict()
check = dict()


def total(arr):
    for item in arr:
        eat, calories = item[:item.rfind(" ")], float(item[item.rfind(" ") + 1:])
        if eat not in menu.keys():
            menu[eat] = calories
        check[eat] = check.get(eat, 0) + 1
    sum_of_kCal = 0
    for item in sorted(list(check.keys())):
        sum_of_kCal += menu[item] * check[item]
        print(f"{item} - {check[item]} - {round(menu[item] * check[item], 1)} kCal")
    print("------")
    print(f"Total: {round(sum_of_kCal, 1)} kCal")
    print()

data = ["Ice cream, strawberry 192",
        "Puff pastry with protein cream 461"]
total(data)
data = ["Orange juice drink 54.5",
        "Ice cream, strawberry 192",
        "Puff pastry with protein cream 461"]
total(data)