'''
    Decorators :
    decorators are used to change behaviour of a function without changing the function itself.
    decorators are used to add functionality to an existing function.

    functions are taken as arguments into another function and then called inside the wrapper function.
    decorators are defined with @ symbol.
    
    inner functin
    
    decorator requires nested functions.

'''


    

#4
def throw_party(func): #func --> order_pizza
    
    def inner(): #6
        print("i got decorated") #7
        func() #it will call order_pizza() #8
        
    return inner   #5  

@throw_party #decorator #3
def order_pizza(): #2
    print("pizza ordered")  #9      
    

order_pizza()     # 1
 

 
 
 
 


