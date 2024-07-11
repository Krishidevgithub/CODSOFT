print("*******************************<SIMPLE BASIC CALCULATOR>************************************************************")
print("--------------------------------------------------------------------------------------------------------------------------------------------")
num1=float(input("Enter the first number: "))          #Enter the first number to perform calculation
num2=float(input("Enter the second number: "))         #Enter the second number to perform calculation
print("--------------------------------------------------------------------------------------------------------------------------------------------")
operator = input("Enter an operator for calculation(+ - * / **): ")   #Enter the valid operator for calculation
print("--------------------------------------------------------------------------------------------------------------------------------------------")
#Operations performed by each operator
if operator=="+":
    result=num1 + num2                            #Add two numbers
    print("Result:", round(result, 3))                       #Give the sum of two numbers
    print("------------------------------------------------------------------------------------------------------------------------------------")
elif operator=="-":
    result=num1-num2                              #Subtract two numbers
    print("Result:", round(result, 3))                       #Give the difference between two numbers
    print("--------------------------------------------------------------------------------------------------------------------------------------------")
elif operator=="*":
    result=num1* num2                             #Multiply two numbers
    print("Result:", round(result, 3))                       #Give the product of two numbers
    print("--------------------------------------------------------------------------------------------------------------------------------------------")
elif operator=="/":
    result=num1/num2                              #Divide two numbers
    print("Result:", round(result, 3))                       #Give the quotient of two numbers
    print("--------------------------------------------------------------------------------------------------------------------------------------------")
elif operator=="**":
    result=num1**num2                 #Squares up a number(num1) to num2 times
    print("Result:", round(result, 3))           #Give the square of a number
    print("--------------------------------------------------------------------------------------------------------------------------------------------")
else:
    print("Enter a valid operator to perform the operation")     #Invalid operator

print("########################################PROCESS FINISHED##########################################")