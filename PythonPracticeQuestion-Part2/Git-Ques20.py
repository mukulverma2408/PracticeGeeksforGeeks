#Define a function which can print a dictionary where the keys are numbers between 1 and 3 (both included)
# and the values are square of keys.

def printDict():
    dct = {}
    for  i in range(1,4):
        dct[i] = i**2
    print(dct)

printDict()
