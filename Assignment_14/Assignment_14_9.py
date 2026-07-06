# Write a lambda function which accepts tow numbers
# and returns multiplication

multiplication = lambda no1,no2 : no1*no2

def main():   
    no1 = int(input("Enter number:"))
    no2 = int(input("Enter number:"))

    print("Multiplication is: ",multiplication(no1,no2))
if __name__ == "__main__":
    main()