class Animal:
    def __init__(self, name):
        self.name = name
    def move(self):
        print(self.name, "moved")
class Dog(Animal):
    def __init__(self,name):
        super().__init__(name)
    def bark(self):
        print(self.name, "barking")
    def move(self):
        super().move()
        print(self.name, "scrolling")

new_dog = Dog("Maya")
new_dog.move()
new_dog.bark()