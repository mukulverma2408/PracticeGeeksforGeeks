#Reverse Dictionary mapping
def ReverseMapping(dict):
    newdict = {}
    for key, value in dict.items():
        newdict[value] = key
    print(newdict)

ReverseMapping({'A': 65, 'B': 66, 'C': 67, 'D': 68})

