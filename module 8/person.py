
class person:
    def  __init__(self, Emri, Mbiemri, Gjatsia,):
        self.Emri = Emri
        self.Mbimeri = Mbiemri
        self.Gjatsia = Gjatsia

    def greet(self):
        print("The name of the person is", self.Emri, "The Surname is", self.Mbimeri, "and the height is", self.Gjatsia)

Uvejsi =  person("Uvjes", "Borovci", "199cm")

print(Uvejsi.greet())