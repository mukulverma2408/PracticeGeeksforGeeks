# Write a Python program to find whether it contains an additive sequence or not
#Having issue with this problem
def AdditiveSeq(num):
    for i in range(len(str(num))):
        sumfirttwo = int(str(num)[i]) + int(str(num)[i+1])
        lenfirsttwo = int(len(str(sumfirttwo)))
        thirdnum = int((str(num)[2:(2+lenfirsttwo)]))
        #firstnum = int(str(num)[0])
        #secondnum = int(str(num)[1])
    print(sumfirttwo)
    print(lenfirsttwo)
    print(thirdnum)

AdditiveSeq(66556)
