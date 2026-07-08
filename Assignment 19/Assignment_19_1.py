# write a program which contains one lambda function which accepts one parameter and return power of two

power =lambda a:a**2

def main():
    Num = int(input("Enter number: "))
    ret = power(Num)
    print(f"Input : {Num}       Output : {ret}")

if __name__ == "__main__":
    main()