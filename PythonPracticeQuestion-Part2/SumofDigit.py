#Write a Python program to compute s the sum of the digits of the number 2**20
def SumofDigit(a, b):
    sum = 0
    num = a ** b
    print("{} power {} is {}".format(a, b, num))
    for i in (str(num)):
        #print(i)
        sum  = sum + int(i)
    print("Sum of the digit of power num is {}".format(sum))

SumofDigit(2,10)