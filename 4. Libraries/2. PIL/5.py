from PIL import Image


def color_gradient(name, *cords, kind="linear", color="r"):
    if kind == "linear":
        im = Image.linear_gradient("L")
    else:
        im = Image.radial_gradient("L")
    im = im.convert("RGB")
    pixels = im.load()
    x, y = im.size
    if color == "r":
        for i in range(x):
            for j in range(y):
                r, g, b = pixels[i, j]
                pixels[i, j] = r - 0, g - 255, b - 255
    elif color == "g":
        for i in range(x):
            for j in range(y):
                r, g, b = pixels[i, j]
                pixels[i, j] = r - 255, g - 0, b - 255
    else:
        for i in range(x):
            for j in range(y):
                r, g, b = pixels[i, j]
                pixels[i, j] = r - 255, g - 255, b - 0
    im = im.crop(*cords)
    im.save(name)


color_gradient("/Users/alekseverevkin/Desktop/Coding/YandexLMS/4. Libraries/2. PIL/out5.png", (0, 56, 256, 256))
