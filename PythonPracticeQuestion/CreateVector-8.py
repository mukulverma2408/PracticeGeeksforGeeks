#Write a NumPy program to add a vector to each row of a given matrix
import numpy as np
m = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
v = np.array([1, 1, 0])
m = m + v
print(m)
