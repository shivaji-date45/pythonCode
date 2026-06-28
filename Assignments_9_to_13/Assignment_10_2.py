# Write a program which accepts one number 
# and prints sum of first N natural numbers

def SumOfNaturalNumber(No):
    sum=int((No*(No+1))/2)
    return sum


def main():
    No=int(input("Enter number: "))
    
    print("Sum of natural numbers", SumOfNaturalNumber(No))

if __name__ == "__main__":
    main()    