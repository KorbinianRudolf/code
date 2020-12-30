def quersumme(zahl):
    result = 0
    while zahl:
        result += zahl % 10
        zahl = int(zahl / 10)
    return result


ls = set()

for day in range(1, 32):
    for month in range(1, 13):
        for bday in range(21, 31):
            for time in range(0, 25):
                helpv = day + month + bday + time
                res1 = quersumme(helpv)
                res = helpv - res1
                ls.add(res)


print(ls)
print(ls.__len__())
