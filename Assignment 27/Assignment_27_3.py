class Numbers:
    def __init__(self,val):
        self.Value=val
    
    def ChkPrime(self):

        if self.Value <=1:
            return False

        if self.Value == 2:
            return True
    
        for i in range(2,self.Value):
            if self.Value % i == 0:
                return False
        
        return True
        
    def ChkPerfectNumber(self):
        if self.Value <= 1:
            return False
        
        num=int(self.Value/2)

        sum=0
        for i in range(1,num+1):
            if ( self.Value % i == 0):
                sum+=i
        
        if(sum == self.Value):
            return True
        else:
            return False
        
    def Factors(self):

        if self.Value <=0:
            print("Value is not positive integer:")
        else:
            Fctrs=[]

            for i in range(1,self.Value+1):
                if self.Value % i == 0:
                    Fctrs.append(i)

            print(f"Factors of {self.Value} are: {Fctrs}")

    def SumFactors(self):
        sum=0
        if self.Value <=0:
            print("Value is not positive integer:")
        else:       
            for i in range(1,self.Value+1):
                if self.Value % i == 0:
                    sum+=i

        return sum
           


obj1=Numbers(11)
ret=obj1.ChkPrime()
if ret == True:
    print(f"Value : {obj1.Value} is Prime Number")
else:
    print(f"Value : {obj1.Value} is not Prime Number")



obj2=Numbers(28)
ret=obj2.ChkPerfectNumber()
if ret == True:
    print(f"Value : {obj2.Value} is perfect Number")
else:
    print(f"Value : {obj2.Value} is not perfect Number")

obj3= Numbers(10)
obj3.Factors()

sum=obj3.SumFactors()
if sum > 0:
    print(f"Sum of factors: {sum}")