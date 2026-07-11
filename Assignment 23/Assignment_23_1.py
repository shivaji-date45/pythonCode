# Write a Python program using multiprocessing.Pool 
# to calculate the sum of all even numbers from 1 to N for every number from the given list.
# Input
#  Data = [1000000, 2000000, 3000000, 4000000]
# Expected TaskFor each number N, 
#   calculate:(2 + 4 + 6 + ..... + N)
# output
# Process ID : 1234
# Input Number : 1000000
# Sum of Even Numbers : 250000500000

import multiprocessing
import os

isEven =lambda No: No%2 == 0

def sumEven(Num):
    print(f"process is runing pid: {os.getpid()}")
    print(f"Input number : {Num}")

    sum=0

    for i in range(1,Num+1):
        if isEven(i) == True:
            sum+=i
    
    print(f"Sum of Even Numbers: {sum}")

    return sum
    

def main():
    
    Data=[1000000,2000000,3000000,4000000]
    retList=[]

    pObj= multiprocessing.Pool()

    retList= pObj.map(sumEven,Data)

    pObj.close()
    pObj.join()

if __name__ == "__main__":
    main()