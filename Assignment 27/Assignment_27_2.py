class BankAccount:
    ROI=10.5
    def __init__(self,name,amount):
        self.Name=name
        self.Amount=amount

    def Display(self):
        print(f"Account holder name: {self.Name} , Current Balance : {self.Amount}")

    def Deposit(self,amount):
        self.Amount+=amount

    def Withdraw(self,amount):
        if(amount > self.Amount):
            print("You can not withdraw !! your current balance insufficeint")
        else:
            self.Amount-=amount
    
    def CalculateIntrest(self):
        
        intr=(self.Amount*BankAccount.ROI)/100
        return intr

obj1=BankAccount("anbc",10000)
obj1.Display()
obj1.Deposit(1000)
obj1.Display()

interest=obj1.CalculateIntrest()
print(f"interest is {interest}")
obj1.Withdraw(5000)
obj1.Display()


obj2=BankAccount("xyz",20000)
obj2.Display()
obj2.Deposit(1000)
obj2.Display()

interest=obj2.CalculateIntrest()
print(f"interest is {interest}")
obj2.Withdraw(4000)
obj2.Display()