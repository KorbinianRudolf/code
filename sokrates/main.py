from PIL import Image


def main():
    with open('Die Apologie des Sokrates.txt', 'r') as file:
        message = file.read().replace('\n', '')
        img = Image.open('soki.jpg')
        img.convert("RGB")
        mes = [ord(x) for x in message]
        width, height = img.size

        k = 0
        for i in range(0, width - 1):
            for j in range(0, height-1):
                red = mes[k % (len(mes))]
                img.putpixel((i, j), (red, img.getpixel((i, j))[1], img.getpixel((i, j))[2]))
                k = k + 1

        img.save('out.jpg')


if __name__ == "__main__":
    main()
