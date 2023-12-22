class Bank:
    
    
    IFSC = "SBIN0001" #class variable / static variable
    
    def __init__(self,name):
        self.userName = name #instance variable
        


b1 = Bank("raj")        
b2 = Bank("rajvi")
b3 = Bank("rajesh")


Bank.IFSC = "SBIN0002" #this the static way of changing the static variable
#b1.IFSC = "SBIN0003" #this is the instance way of changing the static variable,this one is not recommended
print(b1.userName, b1.IFSC)
print(b2.userName, b2.IFSC)
print(b3.userName, b3.IFSC)

print(Bank.IFSC) #static variable can be accessed using class name
# print(Bank.userName) 