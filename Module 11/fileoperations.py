import os


file_path = "example"



# file_path = "example"
# file = open(file_path,"r")
#
# content = file.read()
# file.close()

# with open(file_path, "r") as file:
#     contact = file.read()
#     print(contact)


#reading from file
with open('example', "r") as file:
    content = file.read() #read entire content
    line = file.readline() #read a single line
    lines = file.readlines() #read all lines into a list

#writing to file
with open('example', 'w') as file:
    file.write("Hello, World") #write date to a file

lines = ["Hello World!\n", "Welcome to Python ADV!\n"]

with open('example', 'r') as file:
    file.seek(0)
    data = file.read()
    print(data)



#Me kqyr a ekziston file
if os.path.exists('example'):
    print("file exists")

with open('example', 'a') as file:
    file.write("\nNew data append")

#Reading and writing in some binary data

data = b'This is some binary data'
with open('example', 'wb') as file:   #wb Write Binary
    file.write(data)

with open('binary_file.bin', 'rb') as binary_file:
    data = binary_file.read()
