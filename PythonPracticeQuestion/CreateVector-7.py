#Write a NumPy program to compute sum of all elements, sum of each column and sum of each row of a given array
import numpy as np
arr = np.arange(1,10).reshape(3,3)
print(arr)
print(arr[0,:])
sum_row = sum(arr[0,:])
print(sum_row)