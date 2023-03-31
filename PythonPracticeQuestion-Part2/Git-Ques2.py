#Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the area.

class Circle:
    def __init__(self, r):
        self.radius = r

    def area(self):
        return 3.14*self.radius**2

cir = Circle(5)

print(cir.area())
print(cir.radius)