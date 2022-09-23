#Create an inner function
def Outer(x, y):
    def Inner(x, y):
        return (x+y)
    z = Inner(x, y)
    return (z+'Developer')

print(Outer('Mukul', 'Verma'))

