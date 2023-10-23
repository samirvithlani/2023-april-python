
#local variable --{} -->
#global variable -> global

def outer():
    
    # inner()
    print("Outer function")
    
    def inner():
        #20
        print("Inner function")
        
    inner()        
    
    #20
    inner()


outer()    




def outer1(x):
    
    print("Outer function")
    print("x -",x)
    def inner1(x1):
        print("Inner function")
        print("x1 -",x1)
    
    
    inner1(x)


outer1(100)       



# def outer2(x,y):
    
#     def inner2(x1):
#         return x1 **2
    
    
#     ans = inner2(x+y)
#     print("ans...",ans)


# outer2(2,4)    

# def outer2(x,y):
    
#     def inner2(x1):
#         return x1 **2
    
    
#     ans = inner2(x+y)
#     #print("ans...",ans)
#     return ans

# ans = outer2(2,4)    
# print("ans...",ans)

def outer2(x,y):
    
    def inner2(x1):
        return x1 **2
    
    
    # ans = inner2(x+y)
    # print("ans...",ans)
    
    return inner2(x+y)


ans = outer2(2,4)    
print("ans...",ans)