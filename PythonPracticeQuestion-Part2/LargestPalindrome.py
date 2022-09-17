#Write a Python program to find the largest palindrome made from the product of two 4-digit numbers.
n = 0
for i in range(9999, 1000, -1):
    for j in range(i, 1000, -1):
        prod = i * j
        if (str(prod) == str(prod)[::-1]) and (prod > n):
            n = prod
print(n)


