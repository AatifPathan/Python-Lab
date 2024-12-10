class Rectangle:
    def __init__(self):
        self.l=4
        self.b=8
    def area(self):
        return self.l*self.b
r1=Rectangle()
print(f"Area using default constructor: {r1.area()}")  
