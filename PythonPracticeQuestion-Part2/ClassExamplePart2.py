from ClassExample import Vehicle, ElectricVehicle
gas_fleet = []
electric_fleet = []

for _ in range(100):
    vehicle = Vehicle('Honda', 'Civic', 'car')
    gas_fleet.append(vehicle)

for _ in range(50):
    evehicle = ElectricVehicle('Nissan', 'Leaf', 'Car')
    electric_fleet.append(evehicle)

for vehicle in gas_fleet:
    vehicle.fuel_up()

for evehicle in electric_fleet:
    evehicle.charge()

print("Gas Vehicle {}".format(len(gas_fleet)))
print("Electric Vehicle {}".format(len(electric_fleet)))
