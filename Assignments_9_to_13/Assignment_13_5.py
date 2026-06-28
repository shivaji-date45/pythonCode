# Write a program which accepts marks and displays grade.
# conditio Example:
# >= 75 ---> Distinction
# >= 60 ---> First Class
# >= 50 ---> Second Class
# < 50  ---> Fail 

def GetGradeFromMarks(Marks):
    if Marks >= 75:
        return "Distinction"
    elif Marks >= 60 :
        return "First Class"
    elif Marks >= 50 :
        return "Second Class"
    else:
        return "Fail"

def main():    
    Marks=int(input("Enter Marks: "))

    print(GetGradeFromMarks(Marks))

if __name__ == "__main__":
    main()    