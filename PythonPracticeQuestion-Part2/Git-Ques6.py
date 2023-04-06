#Write a program that calculates and prints the value according to the given formula:
#Q = Square root of [(2 * C * D)/H]
#Following are the fixed values of C and H:
#C is 50. H is 30.
#D is the variable whose values should be input to your program in a comma-separated sequence.

import math
def formula():
    c = 50
    h = 30
    op = []
    lst = list(map(int, input("Enter Comma seprated value of d :- ").split(',')))
    for d in lst:
        tmp = round(math.sqrt((2 * c * d)/h),2)
        op.append(tmp)
    return op

print(formula())


