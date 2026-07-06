# Write a lambda function which accepts one number
# and returns true if number is even else false

checkEvenLambda = lambda no1 : True if (no1%2 == 0) else False 

def main():   
    no1 = int(input("Enter number:"))

    print(checkEvenLambda(no1))
if __name__ == "__main__":
    main()