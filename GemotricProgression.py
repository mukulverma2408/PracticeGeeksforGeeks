# Write a Python program to check a sequence of numbers is a geometric progression or not

def GemotricProg(lst):
    firstdiff = lst[1] - lst[0]
    for i in range(1, len(lst)-1):
        diff = lst[i+1] - lst[i]
        #print(lst[i+1], lst[i])
        #print(diff)
        if diff == firstdiff:
            continue
        else:
            return "NotgemotricProgg"
            break

print(GemotricProg([5, 7, 9, 11, 13]))
