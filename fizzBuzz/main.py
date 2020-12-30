def fizzBuzz():

    arr = [(3, "Fizz"), (5, "Buzz"), (7, "Fuzz"), (13, "Bizz")]

    for i in range(100):
        output = ""
        for tup in arr:
            if i % tup[0] == 0:
                output += tup[1]

        if output == "":
            output += str(i)

        print(output)

fizzBuzz()
