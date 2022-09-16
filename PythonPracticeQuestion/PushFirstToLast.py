#Write a Python program to the push the first number to the end of a list
def PushFirstToLast(lst):
    num = lst[0]
    del lst[0]
    lst.append(num)
    return (lst)

print(PushFirstToLast([5, 2, 9, 2, 7, 0, 5, 69]))