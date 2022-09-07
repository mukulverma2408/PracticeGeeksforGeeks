#Write a Python program to check if a number is a perfect square
import math
def PerfectSquare(n):
    num = int(math.sqrt(n))
    #print(num)
    return((num * num) == n)

print(PerfectSquare(9))