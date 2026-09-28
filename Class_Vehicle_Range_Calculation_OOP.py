class Vehicle:
    def __init__(self,id_number,fuel,mileage):
        self.id_number=id_number
        self.fuel=fuel
        self.mileage=mileage
    @property
    def Range_Calculation(self):
        if self.fuel <= 150 :
            if self.mileage < 5000 :
                self.range=self.fuel*15*1.05
                print(f'{self.range}km is the range of current car')
            elif self.mileage < 10000:
                self.range = self.fuel * 15 * 1.03
                print(f'{self.range}km is the range of current car')
            elif self.mileage < 20000:
                self.range = self.fuel * 15 * 1.02
                print(f'{self.range}km is the range of current car')
            elif self.mileage > 20000:
                self.range = self.fuel * 15 * 1.00
                print(f'{self.range}km is the range of current car')
        else:
            print(f'{self.fuel} cannot be greater maximum capacity')
class Electric_vehicle(Vehicle):
    def __init__(self,id_number,battery_capacity,mileage):
        super().__init__(id_number,battery_capacity,mileage)
        self.battery_capacity=battery_capacity

    @property
    def Range_Calculation(self):
        if self.battery_capacity <= 150 :
            if self.mileage < 5000 :
                self.range=self.battery_capacity*8*1
                print(f'{self.range}km is the range of current car')
            elif self.mileage < 10000:
                self.range=self.battery_capacity*8*0.96
                print(f'{self.range}km is the range of current car')
            elif self.mileage < 20000:
                self.range=self.battery_capacity * 8 * 0.93
                print(f'{self.range}km is the range of current car')
            elif self.mileage > 20000:
                self.range = self.battery_capacity * 8 * 0.90 # i cannot create mutpile fi else
                print(f'{self.range}km is the range of current car')
        else:
            print(f'{self.battery_capacity}kwh cannot be greater maximum capacity of 150kwh')
car1=Electric_vehicle('abc-3736',567,8000)
car1.Range_Calculation()


