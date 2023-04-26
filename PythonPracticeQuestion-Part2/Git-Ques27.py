#Write a program to compute:
#f(n)=f(n-1)+100 when n>0
#and f(0)=1
#with a given n input by console (n>0).


def computefun(n):
    if n == 0:
        return 0
    else:
        return(computefun(n-1)+100)

n = int(input("Enter a number : "))
print(computefun(n))