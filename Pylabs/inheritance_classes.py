class Vehicle:
    def __init__ (self,make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def move(self):
        print(f"Vehicle {self.make} moved to Mombasa")
class Car(Vehicle):
    def __init__ (self,make, model, year, doors):
        super(). __init__ (make, model, year)
        self.doors = doors
my_car = Car("Ford", "Mustang", 1999, 2)
print(my_car.doors)
my_vehicle = Vehicle("Ford", "KCY", 2010)
my_car.move()
print(my_vehicle.make, my_vehicle.model, my_vehicle.year)