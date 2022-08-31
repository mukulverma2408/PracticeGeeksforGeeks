#Python Progg to add an element into a list at specified index
def insert(lst, obj, index):
    lst.insert(index, obj)
    return lst
print(insert(["A", "B", "C", "E"], "D", 3))