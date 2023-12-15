#1 parent n child...


class Bank:
    
    def openAccount(self):
        print("open account")
    
    def closeAccount(self):
        print("close account")


class SBI(Bank):
    
    def withdraw(self):
        self.openAccount()
        print("withdraw SBI")
        self.closeAccount()
    
    def deposit(self):
        self.openAccount()
        print("deposit SBI")
        self.closeAccount()

class HDFC(Bank):
    
    def withdraw(self):
        self.openAccount()
        print("withdraw HDFC")
        self.closeAccount()
    
    def deposit(self):
        self.openAccount()
        print("deposit HDFC")
        self.closeAccount()



                              

s = SBI()
s.withdraw()
s.deposit()

h = HDFC()
h.deposit()
h.withdraw()