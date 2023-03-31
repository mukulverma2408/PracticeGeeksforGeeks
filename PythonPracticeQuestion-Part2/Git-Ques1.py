#Write a program which can compute the factorial of a given numbers.
#The results should be printed in a comma-separated sequence on a single line.

def fact(num):
    op = 1
    for i in range(num, 0, -1):
        print(i)
        op = op*i
    return op

def FactRecur(num):
    op = 1
    while num > 0:
        op = num * FactRecur(num-1)
        print(op)
        num -= 1
    return op


#print(fact(5))
print(FactRecur(3))