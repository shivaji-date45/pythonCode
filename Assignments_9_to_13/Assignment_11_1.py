# Write a program which accepts one number 
# and check whether it is prime or not

def CheckIsPrimeNumber(No):
    ret= True

    for i in range(2,No):
       if No%i == 0:
           ret = False
           break
    
    return ret
       

def main():
    No=int(input("Enter number: "))

    if CheckIsPrimeNumber(No) == True:
        print("Prime Number")
    else:
        print("Not Prime Number")

if __name__ == "__main__":
    main()    