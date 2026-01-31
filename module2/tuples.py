#array
from traceback import print_tb

fruits =["apple", "banana", "cherry"]
print(fruits)
fruits[1]="orange"
print(fruits)

#tuples

word = ("spam", "eggs", "ham")
#word[1] = "sausage" - tuples nuk ndryshohen eshte diqka e pa ndyshushme
print(word[-1]) #printon elemientin e fundit
print(len(word)) #printon gjatsin e tupless

person = ("Milot", 100, "Engieneer")

name, age, profession = person

print(name, "age is", age, "and profession is", profession)
