#Find Factorial

#Recursion
def Fact(num):
    prod = 1
    for i in range (num):
        prod = num * (Fact(num-1))
    return prod

def FactNormal(num):
    op = 1
    for i in range(num, 1, -1):
        #print("num is {}".format(i))
        op = op * i
        #print("op is {}".format(op))
    return op


print("Answer via recursion", end=' :- ')
print(format(Fact(5)))

print("Answer via Normal", end=' :- ')
print(format(FactNormal(5)))