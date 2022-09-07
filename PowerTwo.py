#Write a Python program to check if a given positive integer is a power of two
def PowerTwo(n):
    while (n%2 == 0 ):
        n = n/2
    return(n == 1)

print(PowerTwo(10))
print(PowerTwo(16))
print(PowerTwo(36))
print(PowerTwo(66))