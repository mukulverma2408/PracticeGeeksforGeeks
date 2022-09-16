#Python Programme to reverse a list

def reverse(lst):
    rev_lst = []
    for i in range (len(lst)-1, -1, -1):
        rev_lst.append(lst[i])
    print(rev_lst)

lst = [1,2,3,4,5,6,7,8,9,10]
reverse(lst)
