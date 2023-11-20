
def orderFood(func):
    
    def inner(x):
        print("i am ordering food : ",x)
        func(x)
    
    return inner    


@orderFood
def throw_party(x):
    print("Let's throw a party!")
    

throw_party("Pizza")    