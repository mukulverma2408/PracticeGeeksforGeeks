#With a given list [12,24,35,24,88,120,155,88,120,155],
# write a program to print this list after removing all duplicate values with original order reserved.

def RemoveDups(lst):
    newlst = []
    for i in lst:
        if newlst.__contains__(i):
            pass
        else:
            newlst.append(i)
    print(newlst)

lst = [12,24,35,24,88,120,155,88,120,155]
RemoveDups(lst)

lst2 = list(set(lst))
print(lst2)