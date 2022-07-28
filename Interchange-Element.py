#Python Progg to Interchange element is a list
def Interchange_Element(lst):
    print("Element before change {}".format(lst))
    tmp = lst[0]
    lst[0] = lst[-1]
    lst[-1] = tmp
    print("Element after change {}".format(lst))

n = [10, 20, 30, 40, 50]
Interchange_Element(n)
