#Write a Python program to compute the sum of all the multiples of 3 or 5 below 500
counter = 0
for i in range(1,500):
    if (i%3 ==0) or (i%5 ==0):
        counter += i
    else:
        pass
print(counter)