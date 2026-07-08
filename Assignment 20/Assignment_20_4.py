# Design a Python application that creates three threads named Small, Capital, and Digits.
#	All threads should accept a string as input.
#	The Small thread should count and display the number of lowercase characters.
#	The Capital thread should count and display the number of uppercase characters.
#	The Digits thread should count and display the number of numeric digits.
#	Each thread must also display:
#		Thread ID
#		Thread Name

import threading


def Small(str):
    count = 0
    
    for c in str:
        if c >= 'a' and c <= 'z':
            count+=1
    print("Thread Name: Small")
    print(f"Thread ID of Small: {threading.get_ident()}")
    print(f"Count of Small letters: {count}")

def Capital(str):
    count = 0
    
    for c in str:
        if c >= 'A' and c <= 'Z':
            count+=1

    print("Thread Name: Capital")
    print(f"Thread ID Capital: {threading.get_ident()}")
    print(f"Count of Cpaital letters: {count}")
    
def Digits(str):
    count = 0
    
    for c in str:
        if c >= '0' and c <= '9':
            count+=1

    print("Thread Name: Digits")
    print(f"Thread ID Digits: {threading.get_ident()}")
    print(f"Count of Digits: {count}")


def main():
    
    tObj1 = threading.Thread(target = Small,args=("abcndasDFDF1213",))
    tObj2 = threading.Thread(target = Capital,args=("abcndasDFDF1213",))
    tObj3 = threading.Thread(target = Digits,args=("abcndasDFDF1213",))


    tObj1.start()
    tObj2.start()
    tObj3.start()


    tObj1.join()
    tObj2.join()
    tObj3.join()


if __name__ == "__main__":
    main()