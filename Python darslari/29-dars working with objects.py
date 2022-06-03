"""
Working with objects
simple cases
"""

# for only one car:
class Car:
    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        self.year = year
        self.how_long = 0
        self.price = 12_000

    def get_infocar(self):
        return f"Name: {self.name}, Model: {self.model}, Year: {self.year}, Distace travel: {self.how_long}"

    def get_namecar(self):
        return f"{self.name}, {self.model}"

    def get_price(self, price):
        self.get_price = price

    def set_price(self, price):
        self.how_long = price + 1000

    def get_tarvel(self,how_long):
        self.how_long = how_long

class Car_shop():
    def __init__(self, shop_name, direction):
        self.shop_name = shop_name
        self.direction = direction
        self.quantity = 0
        self.list_cars = [] #cars for sale - sotiladigan avtomobillar

    def add_car(self, car):
        self.list_cars.append(car)
        self.quantity += 1
    
    def get_cars_list(self):
        return [one_car.get_infocar() for one_car in self.list_cars]

    
def see_methods(Car_shop):
    return [__doc__ for method in dir(Car_shop) if method.startswith("__") is False]


shop = Car_shop("Auto salon", "tashkent".title())

car1 = Car("Tesla", "X", 2022)
car2 = Car("bmw".upper(), "X7", 2020)
car3 = Car("Mercedes-Benz", "E500", 2000)
shop.add_car(car1)
shop.add_car(car2)
shop.add_car(car3)



# print(shop.get_cars_list())

# print(dir(Car), end='\n\n') #returns only it's <features> due to the reason that we give <a class> to dir() function
# print(dir(Car_shop), end='\n\n')
# print(dir(shop), end='\n\n') #returns not only it's features, but also it's attributes due to the reason that we give <an object> to dir() function
# print(dir(car1), end='\n\n')

print(see_methods(Car_shop)) # !!! MUST BE DONE FROM HERE !!!
