#Please write a program to compute the value of f(n) with a given n input by console.
#Fibonacci Sequence

def print_fibonacci(n):
    op = 0
    if n == 0:
        op = 0
    elif n == 1:
        op =  1
    else:
        op = print_fibonacci(n-1) +  print_fibonacci(n-2)
    return op

print(print_fibonacci(4))
