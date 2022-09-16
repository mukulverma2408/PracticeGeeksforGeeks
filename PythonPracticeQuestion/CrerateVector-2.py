#Write a NumPy program to create a vector with values from 0 to 20 and change the sign of the numbers in the range from 9 to 15
import numpy as np
arr = np.arange(20,40, dtype=int)
print(arr)
for i in range(21):
    if (i > 9) & (i < 16):
        arr[i] *= -1
print(arr)
"""
for i in arr:
    if (i >= 9) & (i <= 16):
        arr[i] = arr[i] * -1

print(arr)
"""