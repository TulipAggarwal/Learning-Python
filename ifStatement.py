#if statements in python, they are the statements in our program that help us to decide between various given conditions

is_tall = False
is_female = True #A boolean variable names is_female
if is_female and is_tall: #executes this code if both of the value of the variables is_female and is_tall is True
    print("You are a female and tall")
elif is_female and not(is_tall):
    print("You are a female but not tall")
elif not(is_female) and is_tall:
    print("You a male and are tall")
else:
    print ("You are a male and not tall") #executes and prints this if both the values are false
#if in line 5 we use or in place of and then line 6 will only execute if any one of both the variables is True