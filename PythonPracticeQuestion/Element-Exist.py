#Python Progg to check if element exist in a list

def check_element (num, lst):
    if num in lst:
        print("Exist")
    else:
        print("Not Exist")
lst = [1,2,3,4,5,6]
check_element(7, lst)


