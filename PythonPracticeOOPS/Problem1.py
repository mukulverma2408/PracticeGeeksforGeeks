class Vechile:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vechile):
    pass

schoolbus = Bus("School Volvo", 180, 12)
