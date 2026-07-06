# Write program which accept one number and return its factorial

def Factorial(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    
    return fact

def main():   
   num=int(input("Enter number: "))
   ret = Factorial(num)

   print(f"Input : {num}        Output : {ret}")

if __name__ == "__main__":
    main()    