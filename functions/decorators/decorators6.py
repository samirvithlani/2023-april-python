def isManager(func):  #getCustomerData
    
    #user dictonry
    def inner(user): #{"id":1,"name":"raj","role":"manager"}
        if(user.get("role")=="manager"):
            print("user is manager...")
            func(user) #getCustomerData
        else:
            print("user is not manager...")    
            
    return inner




@isManager
def getCustomerData(user):
    print("user is manager and he can access Data....")
    #print(user)
    
    

getCustomerData({"id":1,"name":"raj","role":"manager"})    


        
    
        