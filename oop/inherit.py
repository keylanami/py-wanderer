class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def drive(self):
        print(f'{self.brand} {self.model} is driving')

class Electric(Car):
    def __init__(self, brand, model, batterySize):
        super().__init__(brand, model)
        self.batterySize = batterySize
    
    def charge(self):
        print(f'{self.brand} is charging {self.batterySize}-kWh battery')

class Bensin(Car):
    def __init__(self, brand, model, oilgas):
        super().__init__(brand, model)
        self.oilgas = oilgas
    
    def pombensin(self):
        print(f'{self.brand} has its fuel {self.oilgas} Liter')

tesla = Electric('tesla', 'abc', 40)
bmw = Bensin('BMW', 'Series A', 30)

tesla.drive()
bmw.drive()

tesla.charge()
bmw.pombensin()