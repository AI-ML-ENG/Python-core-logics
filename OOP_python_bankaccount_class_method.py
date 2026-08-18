class Bankaccount:
    def __init__(self,total_balance):
        self.total_balance=total_balance
    def action(self):
        while True:
            Action=input(f'enter what you want to do "deposit" or "withdrawal" or "exit" to stop')
            if Action == "deposit":
                deposit=float(input('enter amount to deposit'))
                self.total_balance+=deposit
                return self.total_balance
            elif Action == "withdrawal":
                withdrawal=float(input("enter your amount to withdrawal"))
                if withdrawal > self.total_balance:
                    print('withdrawal amount cannot be greater than total balance')
                elif withdrawal <= self.total_balance:
                    self.total_balance-=withdrawal
                    return self.total_balance
            elif Action == "exit":
                print("thanks for visiting")
                return self.total_balance

moeez=Bankaccount(10000)
print(moeez.action())