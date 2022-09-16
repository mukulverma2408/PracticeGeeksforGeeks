#Write a Python program to find majority element in a list
#[1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 6]

def MajorityElement(lst):
    elementdct = {}
    for i in lst:
        if i in elementdct.keys():
            elementdct[i] +=1
        else:
            elementdct[i] = 1
    #return (elementdct)
    newdct = {k:v for k, v in sorted(elementdct.items(), key = lambda item: item[1])}
    #print(elementdct)
    #print(newdct)
    return(list(newdct.keys())[-1])

lst = [1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 6]
print(MajorityElement(lst))
print(MajorityElement([1,2,3,4,3,3,2,4,5,6,1,2,3,4,6,1,2,3,4,6,6]))