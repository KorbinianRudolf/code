import random
import urllib.request


def pr(args):
    if not args:
        print("No arguments given vor the task\n")
    else:
        out = ""
        for x in args:
            out = out + x
            out = out + " "
        print(out.swapcase())


def spongebob(args):
    if not args:
        print("No arguments given vor the task\n")
    else:
        out = ""
        for x in args:
            z = ''
            for cr in x:
                z = z + cr.swapcase() if bool(random.getrandbits(1)) else z + cr
            out = out + z
            out = out + " "
        print(out)


def getwebsite():
    url = input("Please enter the wanted website\r\n")
    try:
        fp = urllib.request.urlopen(url)
        mybytes = fp.read()
        mystr = mybytes.decode("utf8")
        fp.close()
        print(mystr)
    except ValueError:

        print("Please enter an url in the following form: \r\n")
        print("'http(s):www.WEBSITENAME.TOP_LEVEL_DOMAIN/OPTIONAL_PARAMETERS'")


def weather():
    print("hi")


def exe(coms):
    if coms == []:
        return
    com = coms[0]
    if com == 'print':
        pr(coms.pop())
    elif com == 'sarcasm':
        spongebob(coms.pop())
    elif com == 'web':
        getwebsite()
    elif com == 'weather':
        weather()


# start main part
com = input("Please enter the command\n")
while com != "exit":
    exe(com.split())
    com = input("please enter the command\n")
