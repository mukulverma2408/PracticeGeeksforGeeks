#Write a NumPy program to create a vector of length 5 filled with arbitrary integers from 0 to 10
import numpy as np
arr = np.random.randint(0,6,5)
print(arr)
"""
arr = np.arange(6, dtype=float)
for i in range(6):
    arr[i] = np.random.normal(0,1)
    print(arr[i])
print(arr)
"""