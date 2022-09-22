#Filter dictionary to contain keys present in the given list

def FilterDict(dct, lst):
    newdict = {}
    for key, value in dct.items():
        if key in lst:
            newdict[key] = value
    print(newdict)

d1 = {'A': 65, 'B': 66, 'C': 67, 'D': 68, 'E': 69, 'F': 70}
l1 = ['A', 'C', 'F']

FilterDict(d1, l1)

