#  For every number in the given list, count how many prime numbers exist between 1 and N using multiprocessing Pool.
#  Example
#  10000
#  20000
#  30000
#  40000
import multiprocessing

def isPrime(Num):
    if Num < 2:
        return False
    if Num == 2:
        return True
    
    for i in range(2,Num):
        if Num % i == 0:
            return False
        
    return True

def countOfPrimeNumber(Num):
    
    count = 0
    for i in range(1,Num+1):
        if isPrime(i) == True:
            count+=1
    return count

def main():
    Data=[10000,20000,30000,40000]
    retList=[]

    pObj= multiprocessing.Pool()

    retList= pObj.map(countOfPrimeNumber,Data)

    pObj.close()
    pObj.join()

    print("Input list: ")
    print(Data)
    print("Count of prime numbers in 1 to N :")
    print(retList)

if __name__ == "__main__":
    main()