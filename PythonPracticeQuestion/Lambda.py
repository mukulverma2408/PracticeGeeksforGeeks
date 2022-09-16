#Python sorting string using order defined by another string
str = "eksge"
pat = "asbcklfdmegnot"

priority = list(pat)
dict = {}
for i in range(len(priority)):
    dict[priority[i]] = i
#print(dict)
str = list(str)
str.sort(key = lambda ele: dict[ele])
str.reverse()
print(''.join(str))
