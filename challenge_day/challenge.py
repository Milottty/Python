class Person:
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

        def get_name(self):
            return self.name

        def set_name(self, name):
            self.name = name

        def get_age(self):
            return self.age

        def set_age(self, age):
            self.age = age

        def get_weight(self):
            return self.weight

        def set_weight(self, weight):
            self.weight = weight

        



    def calculate_bmi(self):
        pass

    def get_bmi_category(self):
        pass
    def print_info(self):
        print(f"{self.name} eshte {self.age} vjec, peshon {self.weight} dhe eshte i gjat{self.height}")


class Adult(Person):
    def bmi_cal(self):
        return (self.weight) / (self.weight**2)

    def get_bmi_category(self):
        bmi = self.bmi_cal()
        if bmi < 18.5:
            return "UnderWeight"
        elif bmi <=18.5 < 24.9:
            return "Normal Weight"
        elif bmi < 24.9 < 29.9:
            return "Over Weight"
        else:
            return "Obese"



class Child(Person):
    def bmi_cal(self):
        return (self.weight) / (self.weight**2) * 1.3


    def get_bmi_category(self):
        bmi = self.bmi_cal()
        if bmi < 14:
            return "UnderWeight"
        elif bmi <=14 < 18:
            return "Normal Weight"
        elif bmi < 18 < 24:
            return "Over Weight"
        else:
            return "Obese"