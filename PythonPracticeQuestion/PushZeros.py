#Write a Python program to push all zeros to the end of a list
######PROBLEM#################
def PushZero(lst):
    lstzero = [i for i in lst if i == 0]
    lstnonzero = [i for i in lst if i != 0]
    #print(lstzero)
    #print(lstnonzero)
    lstnonzero.extend(lstzero)
    return (lstnonzero)

print(PushZero([0, 2, 0, 6, 0, 9, 11, 0]))