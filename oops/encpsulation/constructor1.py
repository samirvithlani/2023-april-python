#constructor is special function which has name __init__

#use of constructor is to initialize the instance variable
#constructor is called automatically when object is created
#constructor is called only once for each object
#constructor is optional

#type of constructor
#1. default constructor __init__(self)
#2. parameterized constructor __init__(self,parameter1,parameter2,....)

#self is variable which is used to refer current object of class
class Bank:
    
    balance = 0
    def __init__(self): #b
        #print(self)
        self.balance = 1000 # local variable
        print("I am in default constructor")
    
    
    def getBalance(self): #b
        print(self.balance)
        print("I am in getBalance")


b = Bank()
b.getBalance()
#print("b",b)
#b1 = Bank()
#print("b1",b1)
