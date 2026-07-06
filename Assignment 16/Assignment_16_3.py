# Write a program which contains one function named as Add() which accept two numbers from user
# and return addition of that two numbers

def Add(num1,num2):
    return num1 + num2

def main():   
    num1=int(input("Enter number1: "))
    num2=int(input("Enter number2: "))
    ret = Add(num1,num2)

    print("Addition of two numbers is: ",ret)

if __name__ == "__main__":
    main()    