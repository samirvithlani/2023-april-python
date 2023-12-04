def outer():
    
    def inner():
        print("Inner function")
        
        return 10
    
    
    ans = inner()
    print("ans outer",ans)


outer()    
        