#Python Programme to Print Duplicate from a list
def PrintDuplicate(lst):
    dct = {}
    for i in lst:
        if i in dct.keys():
            dct[i] +=1
        else:
            dct[i] = 1
    #print(dct)
    for j, k in dct.items():
        if k > 1:
            print(j, end=' ')
lst = [1, 4, 1, 5, 6, 4, 9, 10, 9]
PrintDuplicate(lst)