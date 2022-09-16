#Write a NumPy program to create an element-wise comparison (greater, greater_equal, less and less_equal) of two given arrays
import numpy as np
arr1 = np.array([5, 7, 9, 12, 17])
arr2 = np.array([4, 2, 10, 12.00001, 11])
print(np.equal(arr1, arr2))

print(np.allclose(arr1, arr2))