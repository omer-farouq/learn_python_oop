class Car:
    def __init__(self, mk, mdl, yr):
        self.make = mk
        self.model = mdl
        self.year = yr
    
    def move(self):
        print("The car is moving")

    def horn(self):
        print("Beep beep!")

mycar = Car("Subaru", "Forester", 2014)
mycar.horn()

another_car = Car("Camry", 2020)
another_car.move()

print(another_car.model)