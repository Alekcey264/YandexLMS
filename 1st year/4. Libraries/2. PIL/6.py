from PIL import Image


def snow_forest(cords, percent):
    im_of_forest = Image.open("forest.png")

    im_of_snow = Image.open("snow.png").resize((100, 100))
    pixels1 = im_of_snow.load()
    xs, ys = im_of_snow.size
    
    im_of_forest_part = im_of_forest.crop((cords[0], cords[1], cords[0] + 100, cords[1] + 100))
    pixels2 = im_of_forest_part.load()
    
    per = percent / 100
    not_per = 1 - per

    for i in range(xs):
        for j in range(ys):
            r1, g1, b1 = pixels1[i, j]
            r2, g2, b2 = pixels2[i, j]
            new_r = int(r1 * per + r2 * not_per)
            new_g = int(g1 * per + g2 * not_per)
            new_b = int(b1 * per + b2 * not_per)
            pixels1[i, j] = new_r, new_g, new_b 

    im_of_forest.paste(im_of_snow, cords)
    im_of_forest.save("output.png")


snow_forest((450, 300), 30)