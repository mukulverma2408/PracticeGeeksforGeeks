#Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.

def listSquare():
    lst = list(map(int, input("Enter number seperated by comma : ").split(',')))
    lst = [x*x if x%2 ==0 else x for x in lst]
    print(lst)

listSquare()