#Write a Python program to check whether a given number is an ugly number
def UglyNumber(num):
    if num == 1:
        return True
    elif ((num % 2 == 0) or (num % 3 == 0) or (num % 5 == 0)):
        return True
    else:
        return False

print(UglyNumber(1))