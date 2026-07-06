# Write a lambda function which accepts three numbers
# and returns largest number

findMax = lambda no1,no2,no3 : no1 if (no1 >= no2 and no1 >= no3) else (no2 if no2 >= no3 else no3)

def main():   
    no1 = int(input("Enter number:"))
    no2 = int(input("Enter number:"))
    no3 = int(input("Enter number:"))
    print("Max number  is: ",findMax(no1,no2,no3))
if __name__ == "__main__":
    main()