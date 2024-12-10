class Rectangle:
    def __init__(self, length=0, breadth=0):
        self.length = length
        self.breadth = breadth
    def area(self):
        return self.length * self.breadth
r3 = Rectangle(4,6)
print(f"Area computed by the area method: {r3.area()}")  
