
class Demo:
    value=0

    def __init__(self,var1,var2):
        self.no1=var1
        self.no2=var2

    def Fun(self):
        print(f"Value of no1: {self.no1}")
        print(f"Value of no2: {self.no2}")

    def Gun(self):
        print(f"Value of no1: {self.no1}")
        print(f"Value of no2: {self.no2}")


obj1 = Demo(11,21)
obj2 = Demo(51,101)

obj1.Fun()
obj1.Gun()

obj2.Fun()
obj2.Gun()