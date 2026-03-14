from warnings import catch_warnings


class Dog():
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f"{self.name} make the sond : Woof!!")

class Cat():
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f"{self.name} makes the sound: Meoww!")

class Bird():
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f"{self.name} makes the sound: Chirp!")


dog = Dog("BUddy")
cat = Cat("MACA")
bird = Bird("Twitie")

for animal in (dog, cat, bird):
    animal.sound()
