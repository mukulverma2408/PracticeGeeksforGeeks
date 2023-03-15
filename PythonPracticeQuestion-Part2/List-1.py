#Python program to interchange first and last elements in a list
#Input : [12, 35, 9, 56, 24]
#Output : [24, 35, 9, 56, 12]

def ChangeElement(lst):
    tmp = lst[0]
    lst[0] = lst[-1]
    lst[-1] = tmp
    print("First and last element of a list is now replaced")
    return lst


lst = [12, 35, 9, 56, 24]
print(ChangeElement(lst))
