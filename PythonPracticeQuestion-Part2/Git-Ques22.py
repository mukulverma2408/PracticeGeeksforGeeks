#Define a class named Shape and its subclass Square.
# The Square class has an init function which takes a length as argument.
# Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.

class Shape:
    def Area(self):
        print("This is Shapes method")

class Square(Shape):
    def __init__(self, length):
        self.length = length
    def Area(self):
        print("Area of square is {0}".format(self.length*2))

squr = Square(5)
squr.Area()
