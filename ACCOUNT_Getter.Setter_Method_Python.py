class Account:
    def __init__(self,owner_name,balance):
        self.owner_name=owner_name
        self.__balance=balance
    @property
    def Balance(self):
        return self.__balance
    @Balance.setter
    def Balance(self,Amount):
        if Amount < 0:
            print(f'amount cannot be less than 0')
        elif Amount >= 0:
            self.__balance=Amount

    def deposit_money(self,money):
        if money < 1:
            print(f'cannot deposit less than 1')
        elif money >= 1:
            self.__balance+=money
            print(f'deposited {money}')



class Cash_account(Account):
    pass
    def Withdrawal_money(self,amount):
        if amount > self.Balance:
            print(f'amount cannot be greater than {self.Balance}')
        elif amount <= self.Balance:
            self.Balance-=amount
            print(f'{amount} is successfully withdrawal')
per2=Cash_account('moeez',-1)
print(per2.Balance)

per2.Withdrawal_money(100)
per2.deposit_money(6000)
print(per2.Balance)
