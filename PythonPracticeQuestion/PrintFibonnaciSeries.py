#Python Progg to Print Fibonnaci Series

def PrintFibonnaci(number):
    lst = [0]
    for i in range(1,number+1):
        if len(lst) == 1:
            lst.append(1)
        else:
            nxtnum = (lst[i-2] + lst[i-1])
            #print(nxtnum)
            lst.append(nxtnum)
    print(lst)
PrintFibonnaci(12)