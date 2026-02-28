class animals:
    def __init__(self, typeOfAnimal, raca, ngjyra):
        self.typeOfAnimal = typeOfAnimal
        self.raca = raca
        self.ngjyra = ngjyra

    def greet(self):
        print("The type of animal is", self.typeOfAnimal, "The race is ", self.raca, "And the coolor is ", self.ngjyra)

dog = animals("Dog", "Husky", "white")
cat = animals("cat", "british", "Gray")

print(dog.greet())
print(cat.greet())


