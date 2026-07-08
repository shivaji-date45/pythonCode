# Design a Python application that creates two threads named EvenList and OddList.
# 	Both threads should accept a list of integers as input.
# 	The EvenList thread should:
# 		Extract all even elements from the list.
# 		Calculate and display their sum.
# 	The OddList thread should:
# 		Extract all odd elements from the list.
# 		Calculate and display their sum.
# 	Threads should run concurrently.


import threading
from functools import reduce

sum = lambda no1,no2 : no1 + no2

def EvenList(Data):
    
    evenEle=[]
    for num in Data:
        if num %2 == 0:
            evenEle.append(num)

    ans = reduce(sum,evenEle)

    print(f"Input list data: {Data}")
    print(f"Even list data:  {evenEle}")
    print(f"Sum of even elements is: {ans}")

def OddList(Data):
    
    oddEle=[]
    for num in Data:
        if num % 2 != 0:
            oddEle.append(num)

    ans = reduce(sum,oddEle)

    print(f"Input list data: {Data}")
    print(f"Odd list data:  {oddEle}")
    print(f"Sum of odd elements is: {ans}")   


def main():

    Data=[1,2,3,4,5,6,7,8,9]

    tObj1=threading.Thread(target=EvenList,args=(Data,))
    tObj2=threading.Thread(target=OddList,args=(Data,))

    tObj1.start()
    tObj2.start()

    tObj1.join()
    tObj2.join()

if __name__ == "__main__":
    main()