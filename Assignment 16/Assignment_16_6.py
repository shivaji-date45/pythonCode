# Write a program which accept number from user and check whether that number is poistive or negative or zero


def CheckNum(num):   
    if(num == 0):
        print(f"Input : {num}                Output : Zero")
    elif (num > 0):
        print(f"Input : {num}                Output : Positive")
    else:
        print(f"Input : {num}                Output : Negative")



def main():
    num=int(input("Enter number: "))   
    CheckNum(num)

if __name__ == "__main__":
    main()    