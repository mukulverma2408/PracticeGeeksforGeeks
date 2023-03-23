#How to count unique values inside a list

input_list = [1, 2, 2, 5, 8, 4, 4, 8]
dct = {}

for i in input_list:
    if i in dct.keys():
        dct[i] += 1
    else:
        dct[i] = 1

print(dct)
for k,v in dct.items():
    if v == 1:
        print(k)

