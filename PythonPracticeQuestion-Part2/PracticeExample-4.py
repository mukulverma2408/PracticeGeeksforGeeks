#Remove duplicate element from a list
import pandas as pd
def remove_dup(lst):
    mydict = {}
    for i in lst:
        if i in mydict.keys():
            mydict[i] += 1
        else:
            mydict[i] = 1
    print(list(mydict.keys()))

l1 = [1,2,3,2,1]
remove_dup(l1)