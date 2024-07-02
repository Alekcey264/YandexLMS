from PIL import Image, ImageDraw


def stripes(num, size, direction="v"):
    colors = {0: (0, 0, 0), 1: (255, 255, 255)}
    img = Image.new("RGB", size, (0, 0, 0))
    color = 0
    drawer = ImageDraw.Draw(img)
    count = 0
    if direction == "h":
        lenght = size[1] // num
        while count * lenght < size[1]:
            drawer.rectangle(((0, count * lenght), (size[0], (count + 1) * lenght)), colors[count % 2])
            count += 1
    else:
        lenght = size[0] // num
        while count * lenght < size[0]:
            drawer.rectangle(((count * lenght, 0), ((count + 1) * lenght), size[0]), colors[count % 2])
            count += 1
    img.save("/Users/alekseverevkin/Desktop/Coding/YandexLMS/4. Libraries/3. Drawing/out1.png")
    
stripes(5, (600, 400), direction="v")