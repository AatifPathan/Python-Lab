class Car:
    def __init__(self, model):
        self.model = model
        print(f"{self.model} is created.")
    def __del__(self):
        print(f"{self.model} is destroyed.")
car1 = Car("Toyota")
car2 = Car("Honda")
del car1
