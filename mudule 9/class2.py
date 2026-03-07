from warnings import catch_warnings


class Animal:
    def __init__(self, name):
        self.name = name


    def sound(self):
        print("some generic animal sound")

    def description(self):
        print(f"This is a animal named {self.name}")




class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def sound(self):
        super().sound()
        print("WOFFFFF")

    def description(self):
        super().description()
        print(f"Breed: {self.breed}")

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def sound(self):
        super().sound()
        print("Maju")

    def description(self):
        super().description()
        print(f"Color: {self.color}")

animal = Animal("Generic Animal")
print(animal.sound())
print(animal.description())

dog = Dog("Rex", "Golden Retriever")
print(dog.sound())
print(dog.description())

cat = Cat("MACA","Gray")
print(cat.sound())
print(cat.description())