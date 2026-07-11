# Write a program that accepts a list of integers and uses Pool.map() 
# to calculate the sum of squares from 1 to N for every element in the list.
# Example Input
# [1000000,2000000,3000000,4000000]
# output
# [333333833333500000,
#  266666866666700000,
#  ...
# ]

import multiprocessing

def sumSquare(Num):

    sum=0

    for i in range(1,Num+1):
        sum+=i**2
    
    return sum
    

def main():
    
    Data=[1000000,2000000,3000000,4000000]
    retList=[]

    pObj= multiprocessing.Pool()

    retList= pObj.map(sumSquare,Data)

    pObj.close()
    pObj.join()

    print(f"Sum square of list: {retList}")

if __name__ == "__main__":
    main()