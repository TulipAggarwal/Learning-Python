#Building a basic calculator

#We have used a float type variable because int will just discard
#the decimal numbers if ever used in our calculator
x = float(input("Enter your first number: "))
y = float(input("Enter your second number: "))

#In the following line sof code we convert the numbers to str i.e., 
#string type in order to make it compatible with the string that we output

print("Sum of: " + str(x) +" & " + str(y) + " is " + str(x+y)) 
print("Diff of: " + str(x) +" & " + str(y) + " is " + str(x-y))
print("Product of: " + str(x) +" & " + str(y) + " is " + str(x*y))
print("Division of: " + str(x) +" & " + str(y) + " is " + str(x/y))
print("Remainder of: " + str(x) +" & " + str(y) + " is " + str(x%y))