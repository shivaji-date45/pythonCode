# Write a program which accept N numbers from user and store it into list.
# Return addition of all elements from that list

def AdditionOfElements(l1):
    sum=0
    for num in l1:
        sum+=num
    return sum

def main():
    num=int(input("Number of elements: "))
    
    l1=list()

    for i in range(num):
        l1.append(int(input()))
    
    ret = AdditionOfElements(l1)

    print("Addition of elements: ", ret)

if __name__ == "__main__":
    main()