# Write a program which accepts one number 
# and prints count of digits in that number

def GetDigitCountNumber(No):
    count = 0

    if  No == 0:
        count=1
    else:
        if No < 0:
            No=-No

        while No != 0:
            No=int(No/10)
            count=count+1
    
    return count

def main():
    No=int(input("Enter number: "))

    print(GetDigitCountNumber(No))

if __name__ == "__main__":
    main()    