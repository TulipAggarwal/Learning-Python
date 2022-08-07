#Reading files in python (employees.txt)

#Specifying the file name as both of my files are in same directory and specifying the type in which I want to open it by writing r which means 'read'
#also storing our file in a variable named emp_file
emp_file = open("employees.txt", "r") #we can also say 'w' for write, 'a' for append, 'r+' for reading and writing

print(emp_file.readable()) #checking if the file in readable or not

print(emp_file.read()) #will read the entire document

print(emp_file.readline()) #will only read the first line

#if we execute line 9 again and again we will be able to read each line one by one

print(emp_file.readlines()) #will print all lines as a list

#using for loop
for employee in emp_file.readlines():
    print(employee)

emp_file.close() #closing the file