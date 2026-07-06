# Write a lambda function which accepts tow numbers
# and returns addition

addition = lambda no1,no2 : no1+no2

def main():   
    no1 = int(input("Enter number:"))
    no2 = int(input("Enter number:"))

    print("Addition is: ",addition(no1,no2))
if __name__ == "__main__":
    main()