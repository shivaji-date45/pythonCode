# Write a program which accepts one number 
# and prints multiplication table of that number

def GetMultiplicationTable(No):
    Table=list()
    
    for i in range(1,11,1):
        Table.append(i*No)

    return Table


def main():
    No=int(input("Enter number: "))
    mulTable= GetMultiplicationTable(No)
    print(mulTable)

if __name__ == "__main__":
    main()    