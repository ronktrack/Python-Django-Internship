class Publisher:
    name = "tech-max publication"
    def display(self):
        print("Name: ",self.name)

class Book(Publisher):
    pageNo = "250"
    def display1(self):
        print("pageNo: ",self.pageNo)

class Tape(Publisher):
    time = 21
    def display2(self):
        print("Time: ",self.time)

b = Book()
t = Tape()
b.display()
b.display1()
t.display2()