#pip install multipledispatch
from multipledispatch import dispatch

class Shape:
    
    @dispatch(float)
    def area(self,r):
        print("Area of Circle: ", 3.14 * (r * r))
    
    
    @dispatch(int, int)
    def area(self, l, b):
        print("Area of Rectangle: ", l * b)


s = Shape()
s.area(10.0)        
s.area(10,20)




