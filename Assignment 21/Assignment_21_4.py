# Design a Python application that creates two threads.
# Thread 1 should compute the sum of elements from a list.
# Thread 2 should compute the product of elements from the same list.
# Return the results to the main thread and display them.

import threading

def SumOfElem(lst,Result):
    
    sum=0
    for num in lst:
        sum+=num
    
    Result["Sum"]=sum


def ProdOfElem(lst,Result):
    prod=1
    for num in lst:
        prod*=num
    
    Result["Prod"]=prod

def main():
    result={"Sum":None,"Prod":None}
    Data=[10,11,21,31,41]

    tObj1=threading.Thread(target=SumOfElem,args=(Data,result,))
    tObj2=threading.Thread(target=ProdOfElem,args=(Data,result,))

    tObj1.start()
    tObj2.start()

    tObj2.join()
    tObj1.join()

    print(f"Sum value: {result["Sum"]}")
    print(f"Prod value: {result["Prod"]}")

    
if __name__ == "__main__":
    main()