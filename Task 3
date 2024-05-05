#Defining the function for addition
def add(num1,num2):
    "This is to add two input numbers"
    answer=num1+num2
    return answer

#Defining the function for substraction
def substract(num1,num2):
    "This i sto substract two input numbers"
    answer=num1-num2
    return answer

#Defining a function for multiplication
def multiply(num1,num2):
    "This is to multiply two input numbers"
    answer=num1*num2
    return answer

#Defining a function for division
def divide(num1,num2):
    "This is to divide two input numbers"
    answer=num1/num2
    return answer

#Defining a function for finding the power
def power(base_value,power_value):
    "This is to find the power of two input numbers"
    answer=base_value**power_value
    return answer



#--------------------Main Program------------------------------

print("__________________________________________________________")
print("________________SIMPLE CALCULATOR_________________________")


print("Operators\n + ,- , *, /, **")

print()
operator=str(input("Enter the operator : "))

if operator=="+" or operator=="-" or operator=="*" or operator=="/":
    
    #Get the inputs from the user
    num1=float(input("Enter the number 1 : "))
    num2=float(input("Enter the number 2 : "))
    operator=str(input("Enter the operator : "))
    
    #Output the result
    if operator=="+":
        print("The addition of the inputs is : ",add(num1,num2))

    elif operator=="-":
        print("The substraction of the inputs is : ",substract(num1,num2))

    elif operator=="*":
        print("The multiplication of the inputs is : ",multiply(num1,num2))

    elif operator=="/":
        if num2==0:
            print("Cannot divide by zero")
        else:
            print("The division of the inputs is : ",divide(num1,num2))
        
elif operator=="**":
    #Get the inputs from the user and output the results
    base_value=float(input("Enter the base value : "))
    power_value=float(input("Enter the power value : "))
    print("The power of the number is : ",power(base_value,power_value))
    
else:
    print("Invalid operator")
    
    
    
    
