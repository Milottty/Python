#for loop
from itertools import count


# names = ["Milot", "Uvejsi", "Erina", "Blina", "Diar", "Diar B", "Donart"]
#
# for name in names:
#     print(name)
#
# sentence = "Hello Everyone"
#
# for char in sentence:
#     if char.isalpha():
#         print(char)
#
# for number in range(1,10):
#     print(number)
#
#
# numbers = [12, 20, 33, 44, 55, 66, 80, 11, 70, 9, 2]
#
# maximum = numbers[0]
#
# for number in numbers:
#     if number > maximum:
#         maximum = number
#
# print("the maximum value in this array0 was", maximum)


#while loop

count = 1
while count <= 5:
    print("the number is", count)
    count+=1

#break  me dal jasht llop kur e kena mrri targetin

numbers=[1,2,3,4,5,6,7,8,9]
target = 4

for number in numbers:
    if number== target:
        print("target found")
        break

#continue
scores = [68, 54, 21, 13, 67 ,81]
total = 0
count = 0

mesatarja = 0

for score in scores:
    if score<50:
        continue
    total += score
    count+=1

mesatarja = total/count if count>0 else 0
print("Average score abouve 50 is :", mesatarja)


#do while
while True:
    user_input = input("Enter a positive number: ")

    if user_input.isnumeric():
        number = int(user_input)

        if number > 0:
            break
    print("input invalid try again")

print("YOU ENTERD A POSITIVBE NUMBER", number)

total = 0

for number in range(1,11):
    if number%2==0:
        total+=number

print(total)