
def isAlive(func):
    
    def inner(age): #100
        if age>60:
            return func(age*100)
        else:
            return func(age*10)
         
    
    
    return inner



@isAlive
def getPf(age):
    print(age)


getPf(61)    


