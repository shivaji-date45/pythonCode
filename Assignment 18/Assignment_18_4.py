# Write a program which accept N numbers from user and store it into list.
# accpet one another number and return frequency of that number in list 

def FrequncyOfNumberInList(l1,num):
    retList = list(filter(lambda no1: no1== num,l1))

    return len(retList)

def main():
    num=int(input("Number of elements: "))
    
    l1=list()

    for i in range(num):
        l1.append(int(input()))
    
    ele = int(input("Element to search: "))
    ret = FrequncyOfNumberInList(l1,ele)

    print(f"Frequncy of {ele} in list is : ", ret)

if __name__ == "__main__":
    main()