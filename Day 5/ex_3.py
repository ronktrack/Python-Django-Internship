# Create a cal3 class and calculate simple interest

class Cal3:
    i,j,k=0,0,0
    amount = 0
    def __init__(self,a,b,c):
        self.i,self.j,self.k = a,b,c

    def calInterest(self):
        self.amount = self.i*(1 + (self.j*self.k)) # simple interest formula

    def display(self):
        print("Simple Interest is ",self.amount)

a = float(input("Enter balance: "))
b = float(input("Enter rate: "))
c = float(input("Enter time in years: "))
cal = Cal3(a,b,c)
cal.calInterest()
cal.display()