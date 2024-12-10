class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        return self.length * self.breadth
r2=Rectangle(10, 5)
print(f"Area using parameterized constructor: {r2.area()}")  
