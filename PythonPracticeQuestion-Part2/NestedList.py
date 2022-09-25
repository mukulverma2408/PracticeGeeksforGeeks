#Modify the element of a nested list inside the following list
#The solution has resolved using hardcode however that is not correct and look for right solution
def ModifyElement(lst):
    for i in lst:
        if len(i) > 1:
            for j in i:
                print(j)
        else:
            print(i)

lst = [5, [10, 15, [20, 25, [30, 35], 40], 45], 50]
ModifyElement(lst)
