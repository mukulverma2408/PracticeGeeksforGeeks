#Integer Combinations

def IntegerCombination(num1, num2):
    newlst=[]
    for i in range (2, num1):
        for j in range (2, num2):
            newnum = i ** j
            newlst.append(newnum)
    #print(len(newlst))
    newlst = list(set(newlst))
    print(len(newlst))
    print(newlst)

IntegerCombination(21,21)
