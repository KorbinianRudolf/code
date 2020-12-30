
def calc(val):
    return (1 + (1 / val)) ** (1 + val)

def rec(val, rec):
    helpval = val
    for i in range(rec):
        helpval = calc(helpval)

    print("start: " + str(val) + "; end: " + str(helpval))

for i in range(100, 100000, 50):
    rec(i, 6)

