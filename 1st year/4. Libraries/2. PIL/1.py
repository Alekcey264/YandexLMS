from PIL import Image


def wb_negative(name):
    im = Image.open(name)
    pixels = im.load()
    x, y = im.size
    for i in range(x):
        for j in range(y):
            print(pixels[i, j])
            r, g, b = pixels[i, j]
            bw = (r + g + b) // 3
            pixels[i, j] = 255 - bw, 255 - bw, 255 - bw
    im.save('/Users/alekseverevkin/Desktop/Coding/YandexLMS/4. Libraries/2. PIL/out1.png')


wb_negative('/Users/alekseverevkin/Desktop/Coding/YandexLMS/4. Libraries/2. PIL/in1.png')