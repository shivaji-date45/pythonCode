
class Arithmetic:
    def __init__(self):
        self.value1=0    
        self.value2=0   

    def Accpet(self,val1,val2):
        self.value1=val1
        self.value2=val2

    def Addition(self):
        return self.value1 + self.value2

    def Subtraction(self):
        return self.value1 - self.value2

    def Multiplication(self):
        return self.value1 * self.value2

    def Division(self):
        try:
            return self.value1 / self.value2
        except ZeroDivisionError:
             print("Error: Division by zero is not allowed.")
        

obj1=Arithmetic()
obj1.Accpet(11,9)
add=obj1.Addition()
sub=obj1.Subtraction()
mul=obj1.Multiplication()
div=obj1.Division()

print(f"Addition is : {add}")
print(f"Subtraction is : {sub}")
print(f"Multiplication is : {mul}")
print(f"Division is : {div}")

obj2=Arithmetic()
obj2.Accpet(21,51)
add=obj2.Addition()
sub=obj2.Subtraction()
mul=obj2.Multiplication()
div=obj2.Division()

print(f"Addition is : {add}")
print(f"Subtraction is : {sub}")
print(f"Multiplication is : {mul}")
print(f"Division is : {div}")