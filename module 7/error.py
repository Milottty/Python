# try:
#     result=10/0
#
# except ZeroDivisionError:
#     print("Opps! Tried to devide by zero")
#
#
# fruits = {
#     "apple" : 5,
#     "orange" : 3,
#     "banana" : 7
# }
#
# try:
#     print(fruits["cherry"])
#
# except KeyError:
#     print("The key does not match in the dictionary")
#
# text = "THis is not a number"
#
# try:
#     text_to_int = int(text)
#
# except Exception as e:
#     print("an error",e)
#
# try:
#     result = 10/2
# except ZeroDivisionError:
#     print("devison by 0")
# else:
#     print("Devison successful. Result= ", result)
#
# try:
#     result = 10/0
# except ZeroDivisionError:
#     print("devision by 0")
# finally:
#     print("Finally block executed")
#
# def divide_numbers(a,b):
#     try:
#         result = a/b
#         print("the result is ", result)
#     except ZeroDivisionError:
#         print("You tried to divide by 0")
#     except TypeError:
#         print("Invalid Type")
#     except Exception as e:
#         print("Unexpected error", e)
#     else:
#         print("the result is ", result)
#
# divide_numbers(10, 2)
# divide_numbers(10, 0)
# divide_numbers(10, '2')
#



def plus_number(a,b, operator):
    if operator == "+":
        return  a + b
    elif operator == "-":
        return a - b

    elif operator == "*":
        return  a * b
    elif operator == "/":
        return a / b

    else:
        print("KE perdor operator qe nuk ekziston")
try:
    numeri1 = float(input("Type number 1: "))
    numeri2 = float(input("Type number 2: "))
    operator = input("Type the operator you want to put: ")
    result = plus_number(numeri1, numeri2, operator)
    print("THe result of the operation is :", result)
except TypeError:
    print("Duhet te vendosesh numer ")
except ZeroDivisionError:
    print("Nuk lejohet pjestimi me zero")

except Exception as e:
    print("Error", e)

finally:
    print("The code is executed")