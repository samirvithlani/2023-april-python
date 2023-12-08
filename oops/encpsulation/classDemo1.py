#naming convention for class name is CamelCase    UserDetail


class Demo:
    
    #instance variable / class variable
    #local variable
    
    no = 100 #class variable/ instance variable
    
    def getData(self): #self is reference variable which is pointing to current object
        no =150 #local variable
        print("self...",self.no)
        print("no...",no)
        print("I am in getData")


#object creation
d = Demo() # d is object of class Demo /reference variable        
#print(no) #error
print(d.no)
#d.getData(object[d])
d.getData() #calling method using object