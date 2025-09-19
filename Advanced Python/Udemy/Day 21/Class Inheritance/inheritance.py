# Define a base class called Dog
class Dog:
    # Constructor (initializer) method for Dog
    def __init__(self):
        # Every Dog object will have a temperament attribute set to "loyal"
        self.temperament = "loyal"

    # Instance method 'bark' defined for Dog
    def bark(self):
        # Prints a simple barking sound
        print("Woof, woof!")


# Define a subclass Labrador that inherits from Dog
class Labrador(Dog):
    # Constructor for Labrador
    def __init__(self):
        # Call the parent class (Dog) constructor using super()
        # This ensures the Labrador still gets Dog's attributes (like temperament)
        super().__init__()
        # Add a new attribute unique to Labrador
        self.is_a_good_boy = True

    # Override the bark method from Dog
    def bark(self):
        # First, call Dog's version of bark (so it prints "Woof, woof!")
        super().bark()
        # Then, add Labrador-specific behavior: a more polite "bark"
        print("Greetings, good sir. How do you do?")


# Create an instance of the Labrador class
sparky = Labrador()

# Call the bark method on the Labrador object
# This will:
#   1. Execute Dog.bark() → prints "Woof, woof!"
#   2. Then execute Labrador's extra print → "Greetings, good sir. How do you do?"
sparky.bark()
# If you had not called super().bark(), then Labrador.bark()
# would replace/override the parent method completely.
# Since you did call super().bark() first, Labrador.bark() is extending the parent method:
# It runs the parent’s logic and adds more on top.
# Overrides → completely replaces parent behavior.
# Extends → runs parent behavior, then adds new behavior.
# Your Labrador.bark() is an extension of Dog.bark().
