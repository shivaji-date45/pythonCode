#  Write a program that calculates factorials of multiple numbers simultaneously using multiprocessing.Pool.
#  input
#   Data = [10, 15, 20, 25]
#   Expected Task
#   For every N, calculate:
#       N!
# Expected Output Format
#   Process ID : 1240
#   Input Number : 20
#   Factorial : 2432902008176640000

import multiprocessing
import os

def factNum(Num):
    print(f"process is runing pid: {os.getpid()}")
    print(f"Input number is {Num}")
    fact=1
    if Num == 1:
        return 1
    
    if Num == 2:
        return 2
    
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