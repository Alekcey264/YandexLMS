from PIL import Image


def foo(name):
    im = Image.open(name)
    pixels = im.load()
    x, y = im.size
    for i in range(x // 4, x + 1, x // 4):
        for j in range(y // 4, y + 1, y // 4):
            if i == x and j == y:
                break
            im_crop = im.crop((i - x // 4, j - y // 4, i, j))
            im_crop.save(f"image{j // (y // 4)}{i // (x // 4)}.bmp")


foo("image.bmp")