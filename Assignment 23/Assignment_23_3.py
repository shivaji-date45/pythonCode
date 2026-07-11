#  Write a program that counts how many even numbers exist between 1 and N using Pool.map().
#  input
#   Data = [1000000, 2000000, 3000000, 4000000]
# Expected Output Format
#   Process ID : 1236
#   Input Number : 1000000
#   Even Number Count : 500000

import multiprocessing
import os

isEven =lambda No: No%2 == 0

def sumEvenCount(Num):
    print(f"process is runing pid: {os.getpid()}")
    print(f"Input number : {Num}")

    count=0

    for i in range(1,Num+1):
        if isEven(i) == True:
            count+=1
    
    print(f"Even Number Count: {count}")

    return count
    

def main():
    
    Data=[1000000,2000000,3000000,4000000]
    retList=[]

    pObj= multiprocessing.Pool()

    retList= pObj.map(sumEvenCount,Data)

    pObj.close()
    pObj.join()

if __name__ == "__main__":
    main()