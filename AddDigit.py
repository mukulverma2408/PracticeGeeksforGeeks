#Write a Python program to add the digits of a positive integer repeatedly until the result has a single digit
def AddDigit(num):
    while(num > 9):
        op = 0
        lst = list(str(num))
        for i in lst:
            op = op+int(i)
            #print(op)
        num = op
    return op
print(AddDigit(3214532))
