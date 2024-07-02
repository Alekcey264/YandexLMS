from PIL import Image


def less_variety(in_name, out_name):
    colors = set()
    im = Image.open(in_name)
    pixels = im.load()
    x, y = im.size
    for i in range(x):
        for j in range(y):
            r, g, b = pixels[i, j]
            colors.add((r, g, b))
    size = len(colors)
    while size > 256:
        size = size // 2
    print(size)
    im = im.resize((x // 2, y // 2))
    im = im.quantize(size)
    im.save(out_name)
    

less_variety("/Users/alekseverevkin/Desktop/Coding/YandexLMS/4. Libraries/2. PIL/in4.png", "/Users/alekseverevkin/Desktop/Coding/YandexLMS/4. Libraries/2. PIL/out4.png")