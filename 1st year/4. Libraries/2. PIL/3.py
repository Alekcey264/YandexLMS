from PIL import Image


def reflect(name, kind = 1):
    im = Image.open(name)
    if kind == 1:
        im = im.transpose(Image.FLIP_TOP_BOTTOM)
    elif kind == 2:
        im = im.transpose(Image.FLIP_LEFT_RIGHT)
    elif kind == 3:
        im = im.transpose(Image.ROTATE_180)
    im.save("/Users/alekseverevkin/Desktop/Coding/YandexLMS/4. Libraries/2. PIL/out3.png")

reflect("/Users/alekseverevkin/Desktop/Coding/YandexLMS/4. Libraries/2. PIL/in3.png")