# Design a Python application that creates two separate threads named Even and Odd.
# 	. The Even thread should display the first 10 even numbers.
# 	. The Odd thread should display the first 10 odd numbers.
# 	. Both threads should execute independently using the threading module.
# 	. Ensure proper thread creation and execution.

import threading

def DisplayEven():
    number=2
    count=1
    print("Even Data :")

    while count <=10:
        print(number)
        number+=2
        count+=1

def DisplayOdd():
    number=1
    count=1
    print("Odd Data :")

    while count <=10:
        print(number)
        number+=2
        count+=1

def main():
    
    tObj1 = threading.Thread(target=DisplayEven)
    tObj2 = threading.Thread(target=DisplayOdd)

    tObj1.start()
    tObj2.start()

    tObj1.join()
    tObj2.join()


if __name__ == "__main__":
    main()