from PIL import Image
import shutil

greenPic = 'green.jpg'
testPic = 'me.jpg'


def green():
    image = Image.open(greenPic).convert('RGBA')
    pixeldata = list(image.getdata())

    for i, pixel in enumerate(pixeldata):
        r = pixel[:3][0]
        g = pixel[:3][1]
        b = pixel[:3][2]
        state1 = g > r and g > b and g > 75 and r < 130 and b < 130
        if state1:
            pixeldata[i] = (0, 0, 0, 0)

    image.putdata(pixeldata)
    return image


def fuse(pic, overlay):
    picPx = pic.load()
    overlayPx = overlay.load()

    result = pic.copy()
    resultPx = result.load()

    for i in range(overlay.width):
        for j in range(overlay.height):
            if overlayPx[i, j][3] != 0:
                resultPx[i, j] = overlayPx[i, j]

    return result

img = green()
mainPic = Image.open(testPic).convert('RGBA')
fuse(mainPic, img).show()

