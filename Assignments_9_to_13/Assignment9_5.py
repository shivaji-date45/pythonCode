# Write a program which accepts one number
# and check whether it is divisible by 3 and 5

def chkNumberDivisibleBy3and5(No):
    return ( (No % 3 == 0) and (No % 5==0))

def main():
    No=int(input("Enter Number:"))
    ret=chkNumberDivisibleBy3and5(No)
    if (ret == True):
        print("Divisible by 3 and 5")
    else:
        print("Not Divisible by 3 and 5")

if __name__ == "__main__":
    main()    