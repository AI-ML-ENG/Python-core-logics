class Car:
    def __init__(self,brand,model,Hp,torque,speed):
        self.brand = brand
        self.model = model
        self.Hp = Hp
        self.torque = torque
        self.speed = speed

        self.engine=self.Engine(self)
    class Engine:
        def __init__(self,car):
            self.car=car
        def start(self,time):
            self.distance=self.car.speed*time
            return f'{self.distance} in m'
        def d_in_km(self):
            km=self.distance//1000
            return f'{km}km'
car1=Car('BMW','M5_CS',1200,900,300)
car1.engine.start(60)
print(car1.engine.d_in_km())