from PIL import Image


def get_it(name_in, name_out):
    im = Image.open(name_in)
    pixels = im.load()
    x, y = im.size
    for i in range(x):
        for j in range(y):
            r, g, b = pixels[i, j]
            mod = min(abs(255 - r), abs(255 - g), abs(255 - b))
            if abs(255 - r) > mod:
                r += mod
            if abs(255 - g) > mod:
                g += mod
            if abs(255 - b) > mod:
                b += mod
            pixels[i, j] = r, g, b
    im = im.transpose(Image.ROTATE_270)
    im.save(name_out)


get_it("D:\\Yandex LMS\\Test\\img.png", "D:\\Yandex LMS\\Test\\res.png")