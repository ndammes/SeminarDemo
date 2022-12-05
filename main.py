def printBiggerNr(a, b):
    printNr = True

    if printNr == True:
        print("Zahl 1: " + str(a) + ", Zahl 2: " + str(b))
    if a > b:
        return a
    if a < b:
        return b
    else:
        return "a=b"


