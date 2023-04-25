#Define a class named Rectangle which can be constructed by a length and width.
# The Rectangle class has a method which can compute the area.

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print("Area is {0}".format(self.length*self.width))

rect = Rectangle(3,6)
rect.area()