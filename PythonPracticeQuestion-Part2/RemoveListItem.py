#Remove items from a list while iterating
#Not working as expected
def RemoveItem(lst):
    for i in range (len(lst)):
        print("In this Iteration number is {}".format(i))
        if lst[i] > 50:
            lst.remove(lst[i])
            i -= 1
    print(lst)
RemoveItem([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
