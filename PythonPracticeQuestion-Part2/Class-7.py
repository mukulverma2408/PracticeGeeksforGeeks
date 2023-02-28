#Rectangle class

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def Perimeter(self):
        return (2*self.length) + (2*self.width)

    def Display(self):
        print(self.length, self.width)

r1 = Rectangle(3,4)
print(r1.Perimeter())
r1.Display()