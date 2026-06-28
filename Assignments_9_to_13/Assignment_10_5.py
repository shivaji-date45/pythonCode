# Write a program which accepts one number 
# and prints all odd numbers till that number

def getAllOddNumber(No):
    evenList=list()

    for i in range(1,No+1):
        if i%2 != 0:
            evenList.append(i)

    return evenList

def main():
    No=int(input("Enter number: "))
    oddList = getAllOddNumber(No)

    if len(oddList) > 0:
        print(oddList)

if __name__ == "__main__":
    main()    