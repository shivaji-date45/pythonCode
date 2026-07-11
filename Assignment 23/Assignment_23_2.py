# Write a Python program using multiprocessing.Pool 
# to calculate the sum of all odd numbers from 1 to N for every number from the given list.
# Input
#  Data = [1000000, 2000000, 3000000, 4000000]
# Expected TaskFor each number N, 
#   calculate:(1 + 3 + 5 + ..... + N)
# output
# Process ID : 1234
# Input Number : 1000000
# Sum of odd Numbers : 250000500000

import multiprocessing
import os

isOdd =lambda No: No%2 != 0

def sumOdd(Num):
    print(f"process is runing pid: {os.getpid()}")
    print(f"Input number : {Num}")

    sum=0

    for i in range(1,Num+1):
        if isOdd(i) == True:
            sum+=i
    
    print(f"Sum of odd Numbers: {sum}")

    return sum
    

def main():
    
    Data=[1000000,2000000,3000000,4000000]
    retList=[]

    pObj= multiprocessing.Pool()

    retList= pObj.map(sumOdd,Data)

    pObj.close()
    pObj.join()

if __name__ == "__main__":
    main()