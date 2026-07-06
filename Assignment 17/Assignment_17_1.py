# Create on module named as Arithmetic which contains 4 functions as Add() for addition, Sub() for subtraction, Mult() for multiplication 
# and Div() for division. All functions accepts two parameters as number and perform the operation.
#  Write on python program which call all the functions from Arithmetic module by accepting the parameters from user

from Arithmetic import Addition,Subtraction,Multiplication,Division


def main():   
    num1=int(input("Enter first number: "))
    num2=int(input("Enter first number: "))

    print("Addition is : ",Addition(num1,num2))
    print("Subtraction is : ",Subtraction(num1,num2))
    print("Multiplication is : ",Multiplication(num1,num2))
    print("Division is : ",Division(num1,num2))



if __name__ == "__main__":
    main()    