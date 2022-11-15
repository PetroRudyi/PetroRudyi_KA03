import math


def task3(n, printString=''):
    dimension = int(math.log10(n)) + 1
    res = 0
    printString += ' ' + str(n) + ' --> '
    for i in range(dimension):
        diff = (n % (10 ** (i + 1)) - n % (10 ** i)) / (10 ** i)
        printString += ' ' + str(diff) + ' +'
        res += diff
    if (int(math.log10(res)) + 1) > 1:
        printString = printString[:-1] + ' = '
        return task3(res, printString=printString)
    else:
        printString += ' = ' + str(res)
        return res, printString


print(task3(16)[1])
print(task3(942)[1])
print(task3(132189)[1])
print(task3(493193)[1])
