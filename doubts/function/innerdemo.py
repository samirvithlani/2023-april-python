def outer():
    print("Outer function")
    def inner():
        print("Inner function")
    
    inner()


outer()        



def outer1(no1):
    print("Outer function",no1)
    #print("outer x",x)
    
    def inner1(x):
        print("Inner function",x)
        print("Inner function",no1)
    
    
    inner1(10)


outer1(100)        