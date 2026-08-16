class Helmet:
    def __init__(self,brand,product,colour,specs,price):
        self.brand=brand
        self.product=product
        self.colour=colour
        self.specs=specs
        self.price=price
    def availability(self):
        return f'The {self.brand} brand product {self.product} is available in karachi and islamabad and lastly lahore'
    def delivery(self):
        available=self.availability()
        return f'{available} \nhome delivery is available for {self.brand} product {self.product}for certain cities like multan,isl,lahr,karachi'
helmet1=Helmet('Vector','Revo','yellow.grey.black-texture','visor,front-open,back-tail',12000)
print(helmet1.delivery())