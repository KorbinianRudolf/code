from PIL import Image

img = Image.open("me.jpg")
newImg = Image.new("RGB", (img.size[0], img.size[1]), "black")
imgPx = img.load()
newPx = newImg.load()

k = 0
m = 0
for i in range(newImg.size[0]):
    for j in range(newImg.size[1]):
        newPx[i, j] = imgPx[i, (j + k) % newImg.size[1]]

    m = m + 1
    if m == 250:
        k = k + 250
        m = 0
newImg.show()
