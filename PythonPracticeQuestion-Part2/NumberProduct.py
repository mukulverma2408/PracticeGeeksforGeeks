# Write a Python program to create a new array such that each element at index i of the new array is the product of all the numbers of a given array of integers except the one at i
#Have Issues understanding
def NumProduct(lst):
    newlst = []
    for i in lst:
        prod = 1
        for j in lst:
            if j != i:
                prod = prod * j
        newlst.append(prod)
    print(newlst)

NumProduct([10, 20, 30, 40, 50])

