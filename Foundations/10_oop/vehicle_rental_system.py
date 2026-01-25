class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower
    
    def get_engine_info(self):
        return f"{self.horsepower} HP Engine"

class Vehicle:
    
    total_vehicles = 1
    
    def __init__(self, brand, model, engine):
        self.total_vehicles += 1
        self.brand = brand
        self.model = model
        self.engine = engine
    
    @classmethod
    def get_total_vehicles(cls):
        return cls.total_vehicles
    
    def get_details(self):
        return [self.brand, self.model, self.engine.get_engine_info()]
    
    @staticmethod
    def get_vehicle_type():
        return "Generic Vehicle"
    
    @property
    def rental_price(self):
        return self.rental_price
    
    @rental_price.setter
    def rental_price(self, rental_price):
        if (rental_price > 0):
            self.rental_price = rental_price
        
class Car(Vehicle):
    def __init__(self, brand, model, engine, seats):
        super().__init__(brand, model, engine)
        self.seats = seats
    
    def get_details(self):
        details = super().get_details()
        details.append(f"Seats: {self.seats}")
        return details

car = Car("Toyota", "Corolla", Engine(200), 5)
print(car.get_details())
print(car.get_total_vehicles())
car.rental_price(100)
car.rental_price(-1000)
print(car.rental_price())