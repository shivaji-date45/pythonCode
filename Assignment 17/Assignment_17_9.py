# Write program which accept one number and return number of digit in number

def countOfDigit(num):
    count=0
    for i in str(num):
        count+=1

    return count

def main():   
   num=int(input("Enter number: "))
   ret = countOfDigit(num)

   print(f"Input : {num}        Output : {ret}")
if __name__ == "__main__":
    main()    