# Create a cal4 class and calculate square of a number

class Cal4:
    n = 0
    def setdata(self,a):
        self.n = a

    def display(self):
        square = self.n*self.n
        print("square of ",self.n," is ",square)

n = int(input("Enter a number: "))
cal = Cal4()
cal.setdata(n)
cal.display()