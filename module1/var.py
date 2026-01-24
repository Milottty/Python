'''

temp = 36.2

name = "Milot"

age = 2


print(temp)

print(type(name) )

print(age)
'''

x = 8
y = 10

result = x+y
print(result)

#update values

age = 30
age += 1
print(age)



#combine values

fist_name = "Milot"
last_name = "Ymeri"

full_name = fist_name+ " " +last_name
print(full_name)

#array (lists)

fav_colors = ["red", "black", "blue", "navy"]
first = fav_colors[0]
second= fav_colors[1]

print(first)
print(second)

#methods for list
#append - me shtu n fund shkurt e shqip

fav_colors.append("orange")
print(fav_colors)

#insert - me shtu me ni vend specifik
fav_colors.insert(2, "white")
print(fav_colors)

#remove

fav_colors.remove("blue")
print(fav_colors)

del fav_colors [1]
print(fav_colors)

#update 
fav_colors[0] = "pink"
print(fav_colors)

