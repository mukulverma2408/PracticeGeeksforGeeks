#Write a Python program to find a missing number from a list
def FindMissing(lst):
    missinglst = []
    start = min(lst)
    end = max(lst)
    for i in range(start+1, end):
        if i not in lst:
            missinglst.append(i)
    print(missinglst)

FindMissing([1,2,5,6,9])