import streamlit as st

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
        return (self.weight) / (self.height**2)

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
        return (self.weight) / (self.height**2) * 1.3


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


st.title("BMI Calculator")

user_name = st.text_input("Enter your name")
user_age = st.number_input("Enter your age", min_value=0)
user_height = st.number_input("Enter your height (meters)", min_value=0.0)
user_weight = st.number_input("Enter your weight (kg)", min_value=0.0)

if st.button("Calculate"):
    if user_name.isalpha() and user_age > 0 and user_height > 0 and user_weight > 0:

        if user_age < 18:
            person = Child(user_name, user_age, user_weight, user_height)
        else:
            person = Adult(user_name, user_age, user_weight, user_height)

        bmi = person.bmi_cal()
        category = person.get_bmi_category()

        st.write("BMI:", bmi)
        st.write("Category:", category)

    else:
        st.error("Invalid input!")