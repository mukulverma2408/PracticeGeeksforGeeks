#Write a Python program to find the single number in a list that doesn't occur twice
def SingleNumber(lst):
    dict = {}
    for i in lst:
        if i in dict.keys():
            dict[i] += 1
        else:
            dict[i] = 1
    for key, value in dict.items():
        if value == 1:
            return key

lst = [1, 1, 1, 2, 2, 2, 3]
print(SingleNumber(lst))