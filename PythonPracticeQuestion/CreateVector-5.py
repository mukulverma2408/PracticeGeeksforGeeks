#Write a NumPy program to create a 5x5 zero matrix with elements on the main diagonal equal to 1, 2, 3, 4, 5
import numpy as np
arr = np.zeros((5,5), int)
#print(arr)
for i in range(0,5):
    arr[i][i] = i+1
print(arr)