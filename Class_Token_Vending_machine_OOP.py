class Token:
    def get_fee(self, amount: float) -> float:
        pass
class Bitcoin(Token):
    def get_fee(self, amount: float) -> float:
        return amount*0.05
class Stablecoin(Token):
    def get_fee(self,amount : float) -> float:
        return 2.0
class Vending_machine:
    def __init__(self, initial_cash: float):
        self.__cash = initial_cash
    @property
    def Balance(self):
        return self.__cash
    def buy_token(self,token_instance,amount:float) -> float :
        fee=token_instance.get_fee(amount)
        self.__cash += amount +fee
    @classmethod
    def setup_empty_machine(cls):
        return cls(0.0)
    


