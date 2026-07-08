# Design a Python application that creates two threads named EvenFactor and OddFactor.
# 	Both threads should accept one integer num as a parameter.
# 	The EvenFactor thread should:
# 		Identify all even factors of the given num.
# 		Calculate and display the sum of even factors.
# 	
# 	The OddFactor thread should:
# 		Identify all odd factors of the given num.
# 		Calculate and display the sum of odd factors.
# 	
# 	After both threads complete execution, the main thread should display the message: "Exit from main"

import threading
from functools import reduce

sum = lambda no1,no2 : no1 + no2

def EvenFactor(num):
    EvenFact = []
    # Loop from 1 to the num to find factors
    for i in range(1, num + 1):
        if num % i == 0 and i % 2 == 0:
            EvenFact.append(i)
            
    Ans = reduce(sum,EvenFact)
    
    print(f"Even factors of {num}: {EvenFact}")
    print(f"Sum of even factors: {Ans}")

def OddFactor(num):
    oddFact = []
    # Loop from 1 to the num to find factors
    for i in range(1, num + 1):
        if num % i == 0 and i % 2 != 0:
            oddFact.append(i)
            
    Ans = reduce(sum,oddFact)
    
    print(f"Odd factors of {num}: {oddFact}")
    print(f"Sum of odd factors: {Ans}")


def main():

    tObj1=threading.Thread(target=EvenFactor,args=(20,))
    tObj2=threading.Thread(target=OddFactor,args=(9,))

    tObj1.start()
    tObj2.start()

    tObj1.join()
    tObj2.join()

    print("Exit from main ")

if __name__ == "__main__":
    main()