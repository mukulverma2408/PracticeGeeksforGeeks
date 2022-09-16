#Python Progg to find smallest number in list

def SmallestNumber(lst):
    lst.sort()
    print("Smallest Number is {}".format(lst[0]))

lst=[6, 2, 4, 56, 73, 1, -99, 256, -823]
SmallestNumber(lst)
