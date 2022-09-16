#Write a NumPy program to create an array of all the even integers from 30 to 70
import numpy as np
"""
lst = []
for i in range(30, 71):
    if i % 2 == 0:
        lst.append(i)
#print(lst)
arr = np.array(lst)
print(arr)
"""
arr = np.arange(30, 71, 2)
print(arr)
