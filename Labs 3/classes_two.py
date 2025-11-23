# Define a class named Car as is
class Car:
    # Constructor method that runs when creating a new Car object
    def __init__(self, name, model):
        # Store the name in the object's attribute
        self.name = name
        # Store the model in the object's attribute
        self.model = model
    # Method that describes the behavior of moving
    def move(self):
        # Print a message showing how this specific car moves
        print(f"{self.name} moves")
# Define a class named Vehicle that inherits from Car
class Vehicle(Car):
    # Constructor method for Vehicle objects
    def __init__(self, name, model):
        # Call the parent (Car) class constructor to initialize name and model
        super().__init__(name, model)
    # Method overriding the move() method from Car class
    def move(self):
        # Print a custom movement message for Vehicle objects
        print(f"{self.name} speed")
# Create a Car object with name "BMW" and model "BMW"
car = Car("BMW", "BMW")
# Call the move() method on the car object (prints a message)
car.move()
# Create a Vehicle object with name "Vezel" and model "BMW"
vehicle = Vehicle("Vezel", "BMW")

# Call the move() method on the vehicle object (prints overridden message)
vehicle.move()

# Call move() again on the same vehicle object
vehicle.move()
