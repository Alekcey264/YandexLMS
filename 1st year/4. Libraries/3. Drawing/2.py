from PIL import Image, ImageDraw


def train(name, blue="#CCECFF", yellow="#FFC000", dark_blue="#0070C0", green="#548235", 
          orange="#C55A11", size=(280, 200)):
    img = Image.new("RGB", size, blue)
    drawer = ImageDraw.Draw(img)

    drawer.rectangle(((40, 110), (80, 150)), orange)
    drawer.rectangle(((80, 90), (160, 150)), dark_blue)
    drawer.rectangle(((160, 50), (240, 150)), green)
    drawer.rectangle(((185, 60), (215, 100)), (255, 255, 255))
    drawer.rectangle(((150, 40), (250, 50)), orange)
    drawer.rectangle(((80, 60), (110, 90)), (255, 0, 0))

    drawer.polygon(((80, 60), (95, 34), (110, 60)), yellow)
    drawer.polygon(((40, 110), (60, 75), (80, 110)), yellow)

    drawer.ellipse(((180, 130), (220, 170)), (0, 0, 0))
    drawer.ellipse(((120, 130), (160, 170)), (0, 0, 0))
    drawer.ellipse(((80, 140), (110, 170)), (0, 0, 0))

    img.save(name)

train("/Users/alekseverevkin/Desktop/Coding/YandexLMS/4. Libraries/3. Drawing/out2.png")