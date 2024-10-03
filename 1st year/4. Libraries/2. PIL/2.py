from PIL import Image


def frame(name, lenght):
    im = Image.open(name)
    pixels = im.load()
    x, y = im.size
    im1 = im.crop((x // 3, y // 3, 2 * x // 3, 2 * y // 3))
    pixels = im1.load()
    x, y = im1.size
    sum_of_r = 0
    sum_of_g = 0
    sum_of_b = 0
    for i in range(x):
        for j in range(y):
            r, g, b = pixels[i, j]
            sum_of_r += r
            sum_of_g += g
            sum_of_b += b
    avg_color = [sum_of_r // (x * y), sum_of_g // (x * y), sum_of_b // (x * y)]
    im2 = Image.new("RGB", (x + lenght * 2, y + lenght * 2))
    x2, y2 = im2.size
    pixels2 = im2.load()
    for i in range(x2):
        for j in range(y2):
            pixels2[i, j] = avg_color[0], avg_color[1], avg_color[2]
    im2.paste(im1, (lenght, lenght))

    im2.save('done.png')

frame('/Users/alekseverevkin/Desktop/Coding/YandexLMS/4. Libraries/2. PIL/in2.png', 20)