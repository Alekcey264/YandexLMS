num = int(input())
colors = dict()
for _ in range(num):
    text = input().split("\t")
    for item in text:
        colors[item] = colors.get(item, 0) + 1
image = list()
for text, var in colors.items():
    image.append((var, text))
image.sort(reverse=True)
for i in range(len(image)):
    print(image[i][1])
    if image[i][0] != image[i + 1][0]:
        break 