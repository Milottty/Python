

# def greet():
#     print("Hello world")
#
# greet()
#
# def greet_person(name):
#     print("hello", name)
#
# greet_person("Miloti")
#
# def greet2(name):
#     global message
#     message = f"Helo, {name}"
#     print(message)
# greet2("Dren")
# print(message)
#
# #global mun me perdor edhe mrena edhe jasht funksionit


# greeting = "Hello"
# name = "Uvejs"
#
# def greet():
#     global greeting
#     greeting = "Goodbye"
#
#     name = "Dren"
#
#     message = f"{greeting}, {name}"
#     print(message)
#
# greet()

def greet_person(name, greeting="Hello"):
    message = f"{greeting}, {name}"
    return message
metoda1 = greet_person("Milot")
print(metoda1)

metoda2 = greet_person("Donart", "hi")
print(metoda2)