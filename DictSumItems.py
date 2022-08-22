#Python Progg to sum all items in a dictionary
dict =  {'a': 100, 'b':200, 'c':300}

def SumDictItem(dict):
    sum = 0
    for i,j in dict.items():
        sum += j
    print("Sum of items is {}".format(sum))
SumDictItem(dict)
