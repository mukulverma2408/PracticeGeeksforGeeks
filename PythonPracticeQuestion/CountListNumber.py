#Python Progg to count Even & Odd number in a list
list1 = [2, 7, 5, 64, 14, 13, 45, 56, 95]
def CountEvenOddItem(list):
    evenCount = 0
    oddCount = 0
    for i in list:
        if i % 2 == 0:
            evenCount += 1
        else:
            oddCount += 1
    print("Even Elements are {}, Odd Elements are {}".format(evenCount, oddCount))
CountEvenOddItem(list1)
