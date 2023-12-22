class Amazone:
    
    name = 'Amazone' #class variable / static variable
    
    def __init__(self):
        self.user = 'amit' #instance variable
    
    def getProduct(self):
        print(self.user) #instance variable can be accessed using self
        print(Amazone.name) #class variable can be accessed using class name
        print("product details")
        


a = Amazone()
a.getProduct()        