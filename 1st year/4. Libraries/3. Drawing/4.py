from PIL import Image, ImageDraw


def alien(s: int, black=(0, 0, 0)):
    img = Image.new("RGB", (20 * s, 24 * s), (255, 255, 255))
    drawer = ImageDraw.Draw(img)

    drawer.arc(((3 * s, 5 * s), (17 * s, 20 * s)), 180.0, 360.0, black, int(0.6 * s))
    drawer.arc(((3 * s, 1 * s), (17 * s, 23 * s)), 0.0, 180.0, black, int(0.6 * s))

    drawer.chord(((1 * s, 14 * s), (9 * s, 24 * s)), start=270.0, end=360.0, fill=black)
    drawer.chord(((5 * s, 9 * s), (13 * s, 19 * s)), start=90.0, end=180.0, fill=black)
    drawer.chord(((11 * s, 14 * s), (19 * s, 24 * s)), start=180.0, end=270.0, fill=black)
    drawer.chord(((7 * s, 9 * s), (15 * s, 19 * s)), start=0.0, end=90.0, fill=black)

    drawer.ellipse(((9 * s, 21 * s), (11 * s, 22 * s)), black)
    drawer.ellipse(((6 * s, 15 * s), (7 * s, 16 * s)), (255, 255, 255))
    drawer.ellipse(((13 * s, 15 * s), (14 * s, 16 * s)), (255, 255, 255))

    img = img.crop((0, 4 * s, 20 * s, 24 * s))
    img.save("/Users/alekseverevkin/Desktop/Coding/YandexLMS/4. Libraries/3. Drawing/out4.png")


alien(int(input()))