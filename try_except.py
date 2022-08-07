#Catching error in python through try/except

try:
    value = 10/0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:
    print (err) #simply prints the error we got
except ValueError:   
    print("Invalid Input not an integer")