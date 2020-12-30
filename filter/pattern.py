from PIL import Image

width = 500
height = 500
img = Image.new("RGB", (width, height), "white")


def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


f = fib()
for i in range(width - 1):
    for j in range(height - 1):
        ne = next(f)
        w = (i + ne) % width
        h = (j + ne) % height
        c = ne % 255
        d = (c + ne) % 255
        e = (d + ne) % 255
        img.putpixel((w, h), (c, d, e, 255))

img.show()
