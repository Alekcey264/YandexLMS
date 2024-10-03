from PIL import Image


def autopilot(imaged, color):
    pixels = imaged.load()
    x, y = imaged.size
    size_of = 0
    max_count = (0, 0)
    for k in range(10):
        count = 0
        for i in range(size_of, (x // 10) * (k + 1)):
            for j in range(y):
                r, g, b = pixels[i, j]
                if color[0] == r and color[1] == g and color[2] == b:
                    count += 1
        if count > max_count[1]:
            max_count = (k, count)
        size_of += x // 10
    return max_count[0]


image = Image.open(input())  
color = tuple(map(int, input().split()))  
print(autopilot(image, color))

