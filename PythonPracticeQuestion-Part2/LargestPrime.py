#Find the largest prime factor of a given number

def LargetPrime(num):
    lst = []
    for i in range(2, num):
        if num % i == 0:
            lst.append(i)
    return(max(lst))
print(LargetPrime(330))
