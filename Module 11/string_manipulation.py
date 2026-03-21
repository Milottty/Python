with open('example', 'r') as file:
    for line in file:
        cleaned_line = line.strip()
        print(cleaned_line)

with open('example','r') as file:
    for line in file:
        words=line.strip().split()
        print(words)


#Bashkimi i stringut
name = "Milot"
age = 18
with open('output','w') as file:
    file.write("Name: "+name +"\n")
    file.write("Age: "+str(age) + "\n")

#fromatting strings

with open('output', 'w') as file:
    file.write(f"Name: {name}\n")
    file.write(f"Age: {age}\n")

with open('example','r+') as file:
    for line in file:
        cleaned_line = line.strip()
        modified_line = cleaned_line.replace("Line 1", "Line X")
        file.write(modified_line + "\n")