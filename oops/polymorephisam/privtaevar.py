#define private variable and methods
#2 types of private variable 
#1) private variable: _name
# 2) strong private variable: __name

'''

diff between private and strong private variable
1) private variable can be access outside the class
2) strong private variable can not be access outside the class



'''

class PrivateDemo:
    
    __name = "raj"
    _fname = "kumar"
    lname = "singh"
    
    
    def __init__(self):
        print("PrivateDemo Constructor")
        print(self.__name)
        print(self._fname)
        print(self.lname)

    def __privateMethod(self):
        print("Private Method")

p = PrivateDemo()
print(p.lname)
print(p._fname)
#print(p.__name) #AttributeError: 'PrivateDemo' object has no attribute '__name'
p.__privateMethod() #AttributeError: 'PrivateDemo' object has no attribute '__privateMethod'
        


        
    