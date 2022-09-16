#Write a Python program where you take any positive integer n, if n is even,
# divide it by 2 to get n / 2. If n is odd, multiply it by 3 and add 1 to
# obtain 3n + 1. Repeat the process until you reach 1

def CollatzConjecture(num):
    while (num > 1):
        print(num)
        if (num%2 == 0):
            num = num/2
        else:
            num = (3*num)+1

CollatzConjecture(12)