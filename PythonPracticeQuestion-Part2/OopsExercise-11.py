#Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle.
class Circle:
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return (3.14 * self.radius * self.radius)

    def permieter(self):
        return (2* 3.14 * self.radius)

circle = Circle(8)
print(type(circle).__name__)

print("Area of circle is {} ".format(circle.area()))
print("Perimeter of circle is {}".format(circle.permieter()))