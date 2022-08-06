#Learning more about if statements in python

def max_num (num1, num2, num3): #defining the function max_num
    if (num1 >= num2) and (num1 >= num3): #checking the statement condition for num1
        print("The greatest number is: " + str(num1))
    elif (num2 >= num1) and (num2 >= num3): #checking the statement condition for num2
        print("The greatest number is: " + str(num2))
    else: #checking the statement condition for num3
        print("The greatest number is: " + str(num3))

max_num(444,34,5) #calling the function max_num