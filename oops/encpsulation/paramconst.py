class Java:
    
    #version is user defined parameter
    version = 0
    def __init__(self,version): #local variable
        print("I am in parameterized constructor")
        print("version is",version) #1.8
        self.version = version #instance variable
        
    def printversion(self):
        print("I am in printversion")
        print("version is",self.version)    



j = Java(1.8)        
j.printversion()