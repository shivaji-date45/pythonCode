# Write a program that calculates factorials of multiple numbers simultaneously using Pool.map().
# Input
# [10,15,20,25]
# Display
#   Process ID
#   Input Number
#   Factorial

import multiprocessing
import os

def factNum(Num):
    print(f"process is runing pid: {os.getpid()}")
    print(f"Input number is {Num}")
    fact=1

    for i in range(2,Num+1):
        fact*=i
    
    return fact
    

def main():
    
    Data=[10,15,20,25]
    retList=[]

    pObj= multiprocessing.Pool()

    retList= pObj.map(factNum,Data)

    pObj.close()
    pObj.join()

    print(f"Factorial of multiple numbers: {retList}")

if __name__ == "__main__":
    main()