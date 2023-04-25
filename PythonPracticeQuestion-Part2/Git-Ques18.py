#Define a class, which have a class parameter and have a same instance parameter.

class Vechile:
    def __init__(self, color, category):
        self.color = color
        self.category = category

    def print(self):
        print("Color of the car is " + self.color)
        print("Category of the vechile  is " + self.category)

car = Vechile('red' , 'Suzuki')
car.print()

