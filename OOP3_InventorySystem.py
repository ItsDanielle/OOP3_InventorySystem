class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"
    


car1 = Car("Ford", "Fusion", 2022)
car2 = Car("Audi", "A5", 2023)
car3 = Car("Toyota", "Rav4", 2021)

car_inventory = [car1, car2, car3]

print("Inventory Check:")
for car in car_inventory:
    print(car)