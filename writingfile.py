#writing on files in python

#if we use 'w' in here then it will rewrite the entire file for us
emp_file = open("employees.txt", "a")
empl_file = open("employees1.txt" , "w") #will create a new file

#emp_file.write("G - HR") #G employee will be added again if we run the code again
#emp_file.write("\nF - Customer Service") #will add this employee to a new line using '\n'
#print(emp_file.read())

emp_file.close()