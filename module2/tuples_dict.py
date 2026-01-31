
grades = {
    ("John","Math"): 5,
    ("Drenii","Fizik"): 3,
    ("Uvejsi","Muzik"): 5


}
john_math = grades[("John","Math")]
print("John math grade is", john_math)

grades[("Drenii","Fizik")] = 5
print("Dreni updated fizik grade is", grades[("Drenii","Fizik")])

keys = list(grades.keys())

student, subject = keys[0]
print("First key - student:", student, ", Subject", subject)

