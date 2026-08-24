class Vault:
    def __init__(self,ownership):
        self.__ownership=ownership
        self.security=0
    @property
    def owner(self):
        return f'{self.__ownership} is the owner'
    def __level(self):
        if self.security <= 0:
             print("security cannot be negative")
        elif self.security > 0 and self.security <= 5 :
            print(f'{self.security} is current security level')
        elif self.security > 5:
            print(f'security level cannot be greater than 5')
    @property
    def securitylevel(self):
        return self.__level

per1=Vault('moeez')
print(per1.securitylevel)


