# Write a program which accepts one number 
# and prints binary equivalent

def GetBinaryEquivalentOfNumber(No):
    bin_str=str()
    temp=No

    while temp > 0:
        rem=int(temp%2)
        bin_str=str(rem)+bin_str
        temp=int(temp/2)

    return bin_str


def main():    
    No=int(input("Enter Number: "))

    print("Binary equivalent of number ",No," is: ",GetBinaryEquivalentOfNumber(No))

if __name__ == "__main__":
    main()    