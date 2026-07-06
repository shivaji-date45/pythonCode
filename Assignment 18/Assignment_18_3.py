# Write a program which accept N numbers from user and store it into list.
# Return minimum from list
from functools import reduce

max = lambda no1,no2: no1 if no1 < no2 else no2

def MinimumFromList(l1):
    ret = reduce(max,l1)
    return ret

def main():
    num=int(input("Number of elements: "))
    
    l1=list()

    for i in range(num):
        l1.append(int(input()))
    
    ret = MinimumFromList(l1)

    print("Minimum from list is : ", ret)

if __name__ == "__main__":
    main()

