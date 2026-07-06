# Write program which accept one number and return addition of digit in that number
# e.g Input : 123       Output : 6

def sumOfDigit(num):
    sum=0
    for i in str(num):
        sum+=int(i)

    return sum

def main():   
   num=int(input("Enter number: "))
   ret = sumOfDigit(num)

   print(f"Input : {num}        Output : {ret}")
if __name__ == "__main__":
    main()    