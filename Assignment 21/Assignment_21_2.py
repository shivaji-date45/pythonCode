# Design a Python application that creates two threads.
# 	Thread 1 should calculate and display the maximum element from an list.
# 	Thread 2 should calculate and display the minimum element from the same list.
# 	The list should be accepted from the user.

import threading
from functools import reduce

max = lambda no1,no2 : no1 if no1 > no2 else no2
min = lambda no1,no2 : no1 if no1 < no2 else no2

def MaxElementFromList(lst):
    ans = reduce(max,lst)
    print(f"Max element: {ans}")

def MinElementFromList(lst):
    ans = reduce(min,lst)
    print(f"Min element: {ans}")

def main():

    Data=[]
    num = int(input("Enter the element size list : "))

    for i in range(num):
        Data.append(int(input()))
    
    tObj1=threading.Thread(target=MaxElementFromList, args=(Data,))
    tObj2=threading.Thread(target=MinElementFromList, args=(Data,))

    tObj1.start()
    tObj2.start()

    tObj1.join()
    tObj2.join()

    print("Exit from main ")

if __name__ == "__main__":
    main()