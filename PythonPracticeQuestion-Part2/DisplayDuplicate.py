#Display all duplicate items from a list

def DuplicateItems(lst):
    newlst = list(set([x for x in lst if lst.count(x) > 1]))
    print(newlst)

DuplicateItems([10, 20, 60, 30, 20, 40, 30, 60, 70, 80])