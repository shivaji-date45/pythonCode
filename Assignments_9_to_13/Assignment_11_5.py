# Write a program which accepts one number 
# and checks whether it is palindrome or not.

def IsNumberIsPalindrome(No):
    reverseNum = 0
    tempNo =No

    while tempNo != 0:
        rem = int(tempNo%10)
        reverseNum = reverseNum * 10 + rem
        tempNo=int(tempNo/10)
    
    return reverseNum == No

def main():
    No=int(input("Enter number: "))
    
    if IsNumberIsPalindrome(No) == True:
        print("Palindrome")
    else:
        print("Not Palindrome")

if __name__ == "__main__":
    main()    