#Progg to find max number out of two provided numbers

def FindMax(a,b):
    print("First Number is  : {}".format(a))
    print("Second Number is : {}".format(b))
    if a > b:
        return a
    elif b > a:
        return b
    else:
        print("Both number are equal")
        exit(1)

a = int(input("First Number "))
b = int(input("Second Number "))

print("Max number is {}".format(FindMax(a,b)))