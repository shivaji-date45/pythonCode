# Write a program which accepts one number 
# and prints revers of that number

def GetReverseNumber(No):
    reverseNum = 0

    while No != 0:
        rem = int(No%10)
        reverseNum = reverseNum * 10 + rem
        No=int(No/10)
    
    return reverseNum

def main():
    No=int(input("Enter number: "))

    print(GetReverseNumber(No))

if __name__ == "__main__":
    main()    