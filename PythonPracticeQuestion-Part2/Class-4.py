class X:
    def __init__(self, val):
        self.val = val

def get_index(li, target):
    for index, x in enumerate(li):
        if x.val == target:
            return index
    return -1

li = [1,2,3,4,5,6]

a = list()
for i in li:
    a.append(X(i))
print(a)
print(type(a))

print(get_index(a,3))
