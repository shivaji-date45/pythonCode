# Write a program which accepts one number 
# and prints sum of digits in that number

def GetSumDigit(No):
    sum = 0
    while No != 0:
        sum = sum + (int(No%10))
        No=int(No/10)
    
    return sum

def main():
    No=int(input("Enter number: "))

    print(GetSumDigit(No))

if __name__ == "__main__":
    main()    