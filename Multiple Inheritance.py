class Color:
    def get_color(self):
        return "Red"

class Taste:
    def get_taste(self):
        return "Sweet"

class Apple(Color, Taste):
    print("Apple")

apple = Apple()
print(apple.get_color())  
print(apple.get_taste())  
