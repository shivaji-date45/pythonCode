# Design a Python application that creates two threads named Prime and NonPrime.
# 	Both threads should accept a list of integers.
# 	The Prime thread should display all prime numbers from the list.
# 	The NonPrime thread should display all non-prime numbers from the list.

import threading

def Prime(lst):
    primList=[]
    
    for no in lst:
        isPrime=True
        for i in range(2,no):
            if no%i==0:
                isPrime=False
        
        if isPrime == True:
            primList.append(no)

    print(f"Prime list: {primList}")

def NonPrime(lst):
    nonPrimList=[]
    
    for no in lst:
        isPrime=True
        
        for i in range(2,no):
            if no%i==0:
                isPrime=False
        
        if isPrime == False:
            nonPrimList.append(no)

    print(f"NonPrime list: {nonPrimList}")



def main():
    
    Data=[2, 3, 5, 7, 11, 13, 17, 19, 6, 8, 9, 10, 12, 14, 15, 16]

    tObj1 = threading.Thread(target=Prime,args=(Data,))
    tObj2 = threading.Thread(target=NonPrime,args=(Data,))

    tObj1.start()
    tObj2.start()

    tObj2.join()
    tObj1.join()


if __name__ == "__main__":
    main()