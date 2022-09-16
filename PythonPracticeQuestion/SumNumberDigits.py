#Python Progg to sum numbers digit in list
import math
def SumNumbers(lst):
    newlst = []
    for i in lst:
        if i > 9:
            n = [int(d) for d in str(i)]
            newlst.extend(n)
        else:
            newlst.append(i)
    print(newlst)

lst = [1,23, 456, 897, 94, 0, 3, 5, 10]
SumNumbers(lst)


