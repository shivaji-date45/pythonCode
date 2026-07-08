# Design a Python application that creates two threads named Thread1 and Thread2.
# Thread1 should display numbers from 1 to 50.
# Thread2 should display numbers from 50 to 1 in reverse order.
# Ensure that:
# 	Thread2 starts execution only after Thread1 has completed.
# Use appropriate thread synchronization

import threading

def Thread1(count):
    print("Thread Name: Thread1")
    print(f"Thread ID of Thread1: {threading.get_ident()}")
    for i in range(1,count+1):
        print(i,end=" ")

    print("\n")

def Thread2(count):
   
    print("Thread Name: Thread2")
    print(f"Thread ID Thread2: {threading.get_ident()}")
    for i in range(count,0,-1):
        print(i,end=" ")

    print("\n")
def main():
    tObj1=threading.Thread(target=Thread1,args=(50,))
    tObj2=threading.Thread(target=Thread2,args=(50,))

    tObj1.start()

    tObj1.join()
    
    tObj2.start()

    tObj2.join()

if __name__ == "__main__":
    main()