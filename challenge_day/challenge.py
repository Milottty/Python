class Person:
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

        def get_name(self):
            return self.name

        def set_name(self, new_name):
            self.name = new_name

        def get_age(self):
            return self.age

        def set_age(self, new_age):
            self.age = new_age

        def get_weight(self):
            return self.weight

        def set_weight(self, new_weight):
            self.weight = new_weight

        def get_height(self):
            return self.height

        def set_height(self, new_height):
            self.height = new_height


        



    def calculate_bmi(self):
        pass

    def get_bmi_category(self):
        pass
    def print_info(self):
        print(f"{self.name} eshte {self.age} vjec, peshon {self.weight} dhe eshte i gjat {self.height}")


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


while True:
    user_name= input("Enter your name: ")

    if user_name.isalpha():
        print("Valid input:", user_name)
        break
    else:
        print("Try again! No numbers allowed.")

while True:
    user_age = input("Enter your age: ")

    if user_age.isdigit():
        print("Valid number:", user_age)
        break
    else:
        print("Try again! Only numbers allowed.")

while True:
    user_height = input("Enter your Height (In Centimeters): ")

    if user_height.isdigit():
        print("Valid number:", user_height)
        break
    else:
        print("Try again! Only numbers allowed.")

while True:
    user_weight = input("Enter your Weight (In Kilograms): ")

    try:
        user_weight = float(user_weight)

        if user_weight > 0:
            print("Valid number:", user_weight)
            break
        else:
            print("Your weight needs to be positive. Try again.")

    except ValueError:
        print("Enter a number")

user_age = int(user_age)
user_height = float(user_height)

if user_age < 18:
    person = Child(user_name, user_age, user_weight, user_height)
else:
    person = Adult(user_name, user_age, user_weight, user_height)

bmi = person.bmi_cal()
print("BMI:", bmi)

category = person.get_bmi_category()
print("Category:", category)