#Python Progg to Multiply Number is a list
def MultiplyNumber(lst):
    output = 1
    for i in lst:
        output *= i
    print("Multiplication of all number is {}".format(output))
lst = [1, 2, 3, 4]
MultiplyNumber(lst)
