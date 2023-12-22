class Amazone:
    
    name = 'Amazone' #class variable / static variable
    
    def __init__(self):
        self.user = 'amit' #instance variable
    
    #@staticmethod
    # @classmethod
    def getProduct():
        #print(self.user) #instance variable can be accessed using self
        print(Amazone.name) #class variable can be accessed using class name
        print("product details")
        # a = Amazone()
        # print(a.user)
        


# a = Amazone()
# a.getProduct()        
# a = Amazone()
# a.getProduct()
# a = Amazone()
# a.getProduct()
a = Amazone()
a.getProduct() #a
Amazone.getProduct()