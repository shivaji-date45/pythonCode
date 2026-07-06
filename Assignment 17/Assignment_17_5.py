# Write program which accept one number and check number is prime or not

def CheckPrime(num):
    
    ret = True

    for i in range(2,num):
       if num%i==0:
           ret=False
           break
       
    return ret

def main():   
   num=int(input("Enter number: "))
   ret = CheckPrime(num)
   if(ret == True):
        print(f"Input : {num}        Output : It is prime number")

if __name__ == "__main__":
    main()    