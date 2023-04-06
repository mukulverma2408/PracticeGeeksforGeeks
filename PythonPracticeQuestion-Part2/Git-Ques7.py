#Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array.
# The element value in the i-th row and j-th column of the array should be i*j.
import numpy as np

def genArray():
    x = int(input("Enter value of X : "))
    y = int(input("Enter value of Y : "))

    arr = np.array(x, y)
    print(arr)

genArray()
