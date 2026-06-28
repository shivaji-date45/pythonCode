# Write a program which accepts one number 
# and prints all even numbers till that number

def getAllEvenNumber(No):
    evenList=list()

    for i in range(1,No+1):
        if i%2 == 0:
            evenList.append(i)

    return evenList

def main():
    No=int(input("Enter number: "))
    evenList = getAllEvenNumber(No)

    if len(evenList) > 0:
        print(evenList)

if __name__ == "__main__":
    main()    