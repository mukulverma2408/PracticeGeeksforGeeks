#Write a Python program to check if an integer is the power of another integer.Go to the editor
#Input : 16, 2
def PowerNum(number, n):
    while(number % n == 0 ):
        number = number/n
    return(number == 1)

print(PowerNum(27,3))