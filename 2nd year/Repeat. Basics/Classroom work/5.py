from PIL import Image


def foo(name):
    im = Image.open(name)
    for _ in range(4):
        pixels = im.load()
        x, y = im.size
        check_list = [[0, 0, 0], [0, 0, 0]]
        for i in range(1, x):
            for j in range(y):
                r, g, b = pixels[i - 1, j]
                check_list[0][0] += r
                check_list[0][1] += g
                check_list[0][2] += b
                r, g, b = pixels[i, j]
                check_list[1][0] += r
                check_list[1][1] += g
                check_list[1][2] += b 
            if check_list[0] == check_list[1]:
                check_list = [[0, 0, 0], [0, 0, 0]] 
            else:
                im = im.crop((i, 0, x, y))
                check_list = [[0, 0, 0], [0, 0, 0]]
                break
        im = im.transpose(Image.ROTATE_90)
    im.save("res.png")


foo("image.png")