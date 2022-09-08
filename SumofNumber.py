# Write a Python program to find three numbers from an array such that the sum of three numbers equal to zero.
# #Input : [-1,0,1,2,-1,-4]
def SumNumber(lst):
    lst.sort()
    #return lst
    for i in range(0, len(lst)-2):
        sum = lst[i] + lst[i+1] + lst[i+2]
        if sum == 0:
            return(lst[i], lst[i+1], lst[i+2], sum)
lst = [-1,0,1,2,-1,-4]
print(SumNumber(lst))