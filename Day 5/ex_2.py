# Create a cal2 class and calculate area of a circle

class Cal2:
    radius=0
    def setdata(self):
        r = int(input("Enter radius: "))
        self.radius=r

    def display(self):
        area = 3.14*self.radius * self.radius
        print("area of circle ",area)

c = Cal2()
c.setdata()
c.display()