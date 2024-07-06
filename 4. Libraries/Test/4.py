from PIL import Image, ImageDraw

def spotted_uding(filename, w, *colors):
    im = Image.new("RGB", (10 * w, 4 * w), color=(255, 255, 255))

    drawer = ImageDraw.Draw(im)

    drawer.ellipse(((0, 0), (10 * w, 4 * w)), fill=colors[0])
    drawer.rectangle(((2 * w, int(0.5 * w)), (8 * w, int(3.5 * w))), fill=colors[1])

    drawer.ellipse(((int(2.25 * w), w - w // 4), (int(2.75 * w), w + w // 4)), fill=colors[2])
    drawer.ellipse(((int(4.75 * w), w - w // 4), (int(5.25 * w), w + w // 4)), fill=colors[2])

    drawer.ellipse(((int(3.5 * w), 2 * w - w // 4), (int(4 * w), 2 * w + w // 4)), fill=colors[2])
    drawer.ellipse(((int(6 * w), 2 * w - w // 4), (int(6.5 * w), 2 * w + w // 4)), fill=colors[2])

    drawer.ellipse(((int(4.75 * w), 3 * w - w // 4), (int(5.25 * w), 3 * w + w // 4)), fill=colors[2])
    drawer.ellipse(((int(7.25 * w), 3 * w - w // 4), (int(7.75 * w), 3 * w + w // 4)), fill=colors[2])


    im.save(filename)


spotted_uding('D:\\Yandex LMS\\4. Libraries\\Test\\img.png', 40, '#FFDC33', '#CF6B07', '#AB3B96')