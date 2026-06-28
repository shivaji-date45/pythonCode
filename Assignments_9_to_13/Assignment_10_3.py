# Write a program which accepts one number 
# and prints factorail of that number

def FactorailOfNumber(No):
    if No < 0:
        print("Enter positive number")
        return
    
    fact=1
    for i in range(2,No+1):
        fact=fact*i

    return fact

def main():
    No=int(input("Enter number: "))
    
    print("Factorial of number", FactorailOfNumber(No))

if __name__ == "__main__":
    main()    