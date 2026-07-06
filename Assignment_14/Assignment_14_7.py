# Write a lambda function which accepts one number
# and returns true if number is divisible by 5

divisibleByFiveLambda = lambda no1 : True if (no1%5 == 0) else False 

def main():   
    no1 = int(input("Enter number:"))

    print(divisibleByFiveLambda(no1))
if __name__ == "__main__":
    main()