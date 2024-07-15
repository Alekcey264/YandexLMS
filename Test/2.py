n = int(input())
choices = dict()
for _ in range(n):
    text = input().split(", ")
    poss = text[0]
    prob = int(text[1])
    witch = text[2]

    if witch not in choices:
        choices[witch] = (poss, prob)
    else:
        if prob > choices[witch][1]:
            choices[witch] = (poss, prob)

for key, item in choices.items():
    print(f"{key} - {item[0]}")
