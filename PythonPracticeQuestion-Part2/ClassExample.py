class Vehicle:
    def __init__(self, brand, model, type):
        self.brand = brand
        self.model = model
        self.type = type
        self.gas_tank_size = 14
        self.fuel_level = 0

    def fuel_up(self):
        self.fuel_level = self.gas_tank_size
        print("Gas Tank is now full")

    def drive(self):
        print("The {} is now driving".format(self.model))

    def update_fuel_level(self, new_level):
        if self.new_level > self.gas_tank_size:
            print("Tank Size exceeded")
        else:
            self.fuel_level = new_level

class ElectricVehicle(Vehicle):
    def __init__(self, brand, model, type):
        Vehicle.__init__(brand, model, type)
        self.battery_size = 85
        self.charge_level = 0

    def charge(self):
        self.charge_level = 100
        print("The battery is now charged")

    def fuel_up(self):
        print("No fuel tank, it's an electric vehicle")




"""
vehicle_object = Vehicle('Honda', 'Ridgeline', 'Truck')
print(vehicle_object.brand)
print(vehicle_object.model)
print(vehicle_object.type)

vehicle_object.fuel_up()
vehicle_object.drive()
"""