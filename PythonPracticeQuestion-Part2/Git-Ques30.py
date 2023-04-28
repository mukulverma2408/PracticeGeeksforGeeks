#By using list comprehension, please write a program to print
# the list after removing delete numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155].

lst = [12,24,35,70,88,120,155]
newlst = [ x for x in lst if x%5 != 0 and x%7 != 0]

print(newlst)