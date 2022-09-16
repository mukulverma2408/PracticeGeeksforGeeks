#Write a NumPy program to create a 3X4 array using and iterate over it
import numpy as np

arr = np.arange(10,22).reshape(3,4)
#print(arr)
for i in np.nditer(arr):
    print(i, end=' ')
