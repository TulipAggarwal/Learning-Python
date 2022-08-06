#Building a better calculator
def calc():
    num1= float(input("Enter the first number: "))
    num2= float(input("Enter the second number: "))
    operator= input("Input your operator: ")
    if str(operator)=="+":
        print(num1+num2)
    elif str(operator)=="-":
        print(num1-num2)
    elif str(operator)=="*":
        print(num1*num2)
    elif str(operator)=="/":
        print(num1/num2)
    else: #A test case if the user enters any random thing
        print("Enter a valid operator!")

calc()
