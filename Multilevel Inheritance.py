class Vehicle:
    def start(self):
        return "Started"
class Car(Vehicle):
    def drive(self):
        return "Driving"
class PetrolCar(Car):
    def fueling(self):
        return "Fueling"
civic = PetrolCar()
print(civic.start())  
print(civic.fueling())  
