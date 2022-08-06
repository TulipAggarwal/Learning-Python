#using a return statement in python functions
#We use return statement to get back any information that we want from the program

def cube_num(number):
    return number*number*number #returns the value of number^3
    print("abc") #this statement is useless and it's never going to be executed because return statement will break the code
result = cube_num(4) #storing the value of cube_num 4 in result
print(result) #printing the result
