# Write a lmbda function which accepts two numbers 
# and returns minimum of number 

minimumLambda = lambda no1,no2 : no1 if no1 < no2 else  no2 

def main():   
    no1 = int(input("Enter number:"))
    no2 = int(input("Enter number:"))

    print("minimum  number is: ",minimumLambda(no1,no2))
if __name__ == "__main__":
    main()