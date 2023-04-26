#Please raise a RuntimeError exception.

def printNumber(num):
    if num == 0:
        raise RuntimeError("Something Wrong")
    else:
        print("The number is {}".format(num))

printNumber(0)
