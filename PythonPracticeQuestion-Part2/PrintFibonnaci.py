#Print Fibonacci sequence

def Fibonacci(counter):
    lst = []
    for i in range(1,counter):
        if ((i == 1) or (i == 2)):
            lst.append(i)
            #print(lst)
        else:
            lst.append(lst[i-3] + lst[i-2])
    return (sum(lst))
