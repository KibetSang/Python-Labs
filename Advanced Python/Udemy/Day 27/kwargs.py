class Car:
    def __init__(self, **kwa):
        self.make = kwa.get("make")
        self.model = kwa.get("model")
my_car = Car(model = "Mercedes")
print(my_car.make)
print(my_car.model)