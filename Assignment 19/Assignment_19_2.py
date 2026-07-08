# write a program which contains one lambda function which accepts two parameters and returns its mulitplication

multi =lambda Num1,Num2:Num1*Num2

def main():
    Num1 = int(input("Enter number1 : "))
    Num2 = int(input("Enter number2 : "))

    ret = multi(Num1,Num2)
    print(f"Input : {Num1}  {Num2}       Output : {ret}")

if __name__ == "__main__":
    main()