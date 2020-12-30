import json

entries = []
ENTRIES = "entries"
FILE_NAME = "finance.json"
AMOUNT = 'amount'
PURP = 'purpose'
BUDGET = 'budget'


class Entry:
    def __init__(self, amount, purpose):
        self.amount = round(amount, 2)
        self.purpose = purpose

    def print(self):
        print('<{}, {}>'.format(self.amount, self.purpose))


def save(data):
    with open(FILE_NAME, 'w') as outfile:
        json.dump(data, outfile)


def newentry(data):
    amount = input("please enter the amount you spend: ")
    try:
        purp = input("please enter the purpose for what you spend the money: ")
        newe = Entry(float(amount), purp)
        newe.print()

        entries.append(newe)
        data[ENTRIES].append({
            AMOUNT: amount,
            PURP: purp
        })

    except ValueError:
        print("The amount must be a number")
        newentry(data)


def printall():
    for x in entries:
        x.print()


def setbudget(data):
    budget = input('Please enter your budget: ')
    try:
        data[BUDGET] = round(float(budget), 2)
    except ValueError:
        "please enter a valid number"
        setbudget(data)
    save(data)


def getbudget(data):
    print(data[BUDGET])


def helpn():
    print('entry\r\nprintAll\r\nhelp\r\nsetBudget\r\nentryS\r\ngetBudget\r\nsave\r\nwhatsLeft\r\n')


def calcdiff(data):
    out = 0
    for etr in entries:
        out = out + etr.amount
    left = data[BUDGET] - out
    print("You have {} € left".format(left))

def clearall():
    with open(FILE_NAME, 'w') as outfile:
        json.dump([ENTRIES], outfile)


def exe(coms, data):
    if not coms:
        return
    co = coms[0]
    if co == 'entry':
        newentry(data)
    elif co == 'printAll':
        printall()
    elif co == 'help':
        helpn()
    elif co == 'setBudget':
        setbudget(data)
    elif co == 'entryS':
        newentry(data)
        save(data)
    elif co == 'getBudget':
        getbudget(data)
    elif co == 'save':
        save(data)
    elif co == 'whatsLeft':
        calcdiff(data)
    elif co == 'clearAll':
        clearall()
    else:
        print('command unknown')


def loaddata():
    try:
        with open(FILE_NAME) as js:
            data = json.load(js)
            for p in data[ENTRIES]:
                entries.append(Entry(float(p[AMOUNT]), p[PURP]))
    except (json.decoder.JSONDecodeError, KeyError):  # if entries does not exist
        data = {ENTRIES: []}
    except FileNotFoundError:  # if file does not exist
        data = {ENTRIES: []}
        open(FILE_NAME, "w+").close()  # open file, create it on the run, then close it
    except ValueError:
        print("There is an error with reading the file, check if all 'amounts' are numbers or delete the file")
        data = None
    return data


# start main part
def main():
    data = loaddata()
    if data is None:
        exit(0)
    com = input("Please enter the command: ")
    while com != "exit":
        exe(com.split(), data)
        com = input("please enter the command: ")


if __name__ == "__main__":
    main()
