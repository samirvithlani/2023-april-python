class Product:
    
    name = ""
    price = 0.0
    qty = 0
    colors = []
    
    def __init__(self,name,price,qty,colors):
        self.name = name
        self.price = price
        self.qty = qty
        self.colors = colors
    
    
    def printProductData(self):
        print("name is",self.name)
        print("price is",self.price)
        print("qty is",self.qty)
        print("colors are",self.colors)



p1 = Product("Apple",100.0,10,["red","green","yellow"])
p2 = Product("Samsung",200.0,20,["red","silver","white"])        

p1.printProductData()
p2.printProductData()
        
    
    