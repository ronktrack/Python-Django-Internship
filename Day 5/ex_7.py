# Create a cal6 class and calculate area of a square

class Cal6:
    side, squareArea = 0,0
    def setdata(self):
        a = int(input("Enter side of square :"))
        self.side = a

    def area(self):
        self.squareArea = self.side*self.side

    def display(self):
        print("Area of square is :",self.squareArea)

cal = Cal6()
cal.setdata()
cal.area()
cal.display()