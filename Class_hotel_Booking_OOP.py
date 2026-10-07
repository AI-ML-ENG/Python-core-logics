class Normal_booking:
    def __init__(self,days):
        self.days=days
        self.base_price_1_day=10000
    @property
    def Room(self):
        price=self.base_price_1_day
        if self.days < 3 :
            cost=self.days*price
            return cost
        elif self.days >= 3:
            cost=self.days*price*0.90
            return cost

class Luxury_cabin(Normal_booking):
    pass
    @property
    def Room(self):
        price=self.base_price_1_day
        if self.days < 3 :
            cost=self.days*price*1.50
            return cost
        elif self.days >= 3:
            cost=self.days*price*1.40
            return cost
class Eco_cabin(Normal_booking):
    pass
    @property
    def Room(self):
        price=self.base_price_1_day
        if self.days < 3 :
            cost=self.days*price*0.90
            return cost
        elif self.days >= 3:
            cost=self.days*price*0.80
            return cost
room1=Eco_cabin(4)
print(f'{room1.Room} is for Eco cabin')
room1=Luxury_cabin(4)
print(f'{room1.Room} is for luxury cabin')
room1=Normal_booking(4)
print(f'{room1.Room} is for normal cabin')




