import random


n = int(input())
ingrs = input().split(", ")
start_of, end_of = tuple(map(float, input().split()))
names = list()

for i in range(1, n + 1):
    name = random.choice(ingrs)
    while name in names:
        name = random.choice(ingrs)
    names.append(name)
    ingrs.remove(name)
    number = random.randint(1, 10)
    content = random.uniform(start_of, end_of)
    time = number * content / 10
    print(f"{i}. {name} {number} of pieces, calories {round(content, 1)} "
          f"kkal, cooking time {round(time, 1)}")

