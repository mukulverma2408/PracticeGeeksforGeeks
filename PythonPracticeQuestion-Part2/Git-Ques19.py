#Define a function which can compute the sum of two numbers.

def sumofdigit(num):
    sum = 0
    for i in str(num):
        sum += int(i)
    print("Number is {} and Sum of digit of the number is {}".format(num, sum))

sumofdigit(134223)