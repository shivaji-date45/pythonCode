#  Write a program that calculates
#  (1^5 + 2^5 + 3^5 + .... + N^5)
#  Input 
#    [  1000000,
#       2000000,
#       3000000,
#       4000000]
# Measure total execution time.

import multiprocessing
import time
def countSum(Num):
    sum=1

    for i in range(1,Num+1):
        sum+=i**5

    return sum


def main():
    Data=[1000000,2000000,3000000,4000000]
    retList=[]

    startTime=time.perf_counter()

    pObj= multiprocessing.Pool()

    retList= pObj.map(countSum,Data)

    pObj.close()
    pObj.join()

    endTime=time.perf_counter()

    print("Input list: ")
    print(Data)
    print("Sum of 1^5 + 2^5 + 3^5 + .... + N^5 ")
    print(retList)

    print("Time required  :",endTime-startTime, "sec")
    
if __name__ == "__main__":
    main()