
class Circle:
    PI = 3.14
    def __init__(self):
        self.Radious=0.0
        self.Area=0.0
        self.Circumference=0.0

    def Accept(self,rad):
        self.Radious=rad

    def CalculateArea(self):
        self.Area= self.PI * (self.Radious**2)

    def CalculateCircumference(self):
        self.Circumference= 2 * self.PI * self.Radious

    def Display(self):
        print(f"Radious of circle: {self.Radious}")
        print(f"Area of circle: {self.Area}")
        print(f"Circumference  of circle: {self.Circumference}")


obj1 =Circle()
obj1.Accept(5)
obj1.CalculateArea()
obj1.CalculateCircumference()
obj1.Display()

obj2 =Circle()
obj2.Accept(7)
obj2.CalculateArea()
obj2.CalculateCircumference()
obj2.Display()


obj3 =Circle()
obj3.Accept(9)
obj3.CalculateArea()
obj3.CalculateCircumference()
obj3.Display()


obj4 =Circle()
obj4.Accept(14)
obj4.CalculateArea()
obj4.CalculateCircumference()
obj4.Display()