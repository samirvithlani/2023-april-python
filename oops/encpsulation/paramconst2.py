class Shape:
    
    height = 0
    width = 0
    radius = 0
    def __init__(self,h,w,r):
        self.height = h
        self.width = w
        self.radius = r
        
    def circle(self):
        return 3.14 * self.radius * self.radius
    
    def square(self):
        return self.height * self.height
    
    
    def rectangle(self):
        return self.height * self.width
    


s = Shape(10,20,30)
carea = s.circle()            
print("carea",carea)
sqarea = s.square()
print("sqarea",sqarea)
rectarea = s.rectangle()
print("rectarea",rectarea)