class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

class Bus(Vehicle):
    def seating_capacity(self, capacity=50):
        return Vehicle.seating_capacity(self, capacity)

""" 
bus = Bus('School Volvo', 180, 12)
print("Vehicle Name: {0} Speed:{1} Mileage:{2}".format(bus.name, bus.max_speed, bus.mileage))
"""

bus = Bus("Bus", 180, 12)
car = Vehicle("car", 200, 20)
print(bus.seating_capacity())
print(car.seating_capacity(4))

