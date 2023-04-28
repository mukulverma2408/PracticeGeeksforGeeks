#Please write a binary search function which searches an item in a sorted list.
# The function should return the index of element to be searched in the list.
#li=[2,5,7,9,11,17,222]

import math
def SearchNum(lst, number):
    start = 0
    end = len(lst)
    while end >= start:
        mid = math.floor(int((start+end)/2))
        if lst[mid] == number:
            return mid
        elif number > lst[mid]:
            start = mid + 1
        elif number < lst[mid]:
            end = mid -1
li=[2,5,7,9,11,17,222]
print(SearchNum(li, 2))


