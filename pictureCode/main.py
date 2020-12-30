from PIL import Image

meage = "Hallo Meike :)"


# print(meage)

# res = [ord(x) for x in meage]
# print(res)
# res2 = ''.join(map(chr, res))
# print(res2)


def hide(img, start, end, message):
    mes = [ord(x) for x in message]
    if len(mes) % 3 == 2:
        mes.append(0)
    elif len(mes) % 3 == 1:
        mes.append(0)
        mes.append(0)
    for i in range(start[0], end[0]):
        for j in range(start[1], end[1]):
            if mes:
                b = mes.pop()  # takes last, so later, i have to take the resulting message in reverse
                g = mes.pop()
                r = mes.pop()
                img.putpixel((i, j), (r, g, b))

    return img


def find(img, start, end):
    img.convert("RGB")
    msg = []
    pxls = []
    for i in range(start[0], end[0]):
        for j in range(start[1], end[1]):
            pxl = img.getpixel((i, j))
            pxls.append(pxl)

    # msg.reverse()           # because i took the message from last to first
    pxls.reverse()
    for x in pxls:
        for p in x:
            if p <= 127:
                msg.append(p)
    res2 = ''.join(map(chr, msg))
    return res2


img3 = Image.open('me.jpg')
img2 = hide(img3, (0, 0), (10, 10), meage)
mess = find(img2, (0, 0), (10, 10))
img2.show()
print(mess)
