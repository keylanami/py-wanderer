
class Car:
    def __init__(self, brand, year, mileage, wheels):
        self.brand = brand
        self.year = year
        self.mileage = mileage
        self.wheels = wheels
    
    def info(self):
        print(f'This is a {self.year} {self.brand}')

    def start_engine(self):
        print(f'The {self.brand} engine is running')

    def drive(self, km):
        self.mileage += km

    def odometer(self):
        print(f'Cars Mileage is at {self.mileage} KM')


audi = Car('Audi Q7', '2020', 0, 4)
audi.info()
audi.start_engine()
 
audi.drive(39)
audi.drive(129)
audi.drive(42)
audi.odometer()

print(audi.wheels)


