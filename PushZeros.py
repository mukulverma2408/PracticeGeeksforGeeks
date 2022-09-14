#Write a Python program to push all zeros to the end of a list
######PROBLEM#################
def PushZero(lst):
    for i in lst:
        print(i)
        if i == 0:
            lst.remove(i)
            lst.append(0)
            print(lst)
    print(lst)

PushZero([0, 2, 3, 6, 0, 9, 11, 10])