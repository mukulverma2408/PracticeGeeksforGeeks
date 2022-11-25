class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def Perimeter(self):
        return (2*self.length + 2*self.width)

    def Area(self):
        return (self.length * self.width)

    def display(self):
        print("Length for Rectangle is {}".format(self.length))
        print("Width for Rectangle is {}".format(self.width))
        print("Area for Rectangle is {}".format(self.Area()))
        print("Perimeter for Rectangle is {}".format(self.Perimeter()))

class Parallelepipede(Rectangle):
    def __init__(self, length, width, height):
        Rectangle.__init__(self, length, width)
        self.height = height

    def Volume(self):
        return (self.length * self.width * self.height)


rect = Rectangle(5, 8)
rect.display()

parrpipe = Parallelepipede(7, 5, 2)
print("Volume of Parallelpipede is {}".format(parrpipe.Volume()))