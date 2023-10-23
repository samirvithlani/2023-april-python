#args
#def

# def addUser(user):
#     print("User added: " + user)

def addUser(x,*args):
    #//print("User added: " + args)
    print(x)
    print(args)
    print(type(args))


addUser("John","raj","jay","parth","james","mmm")    

def addEmployee(*emps,x,y):
    print(emps)
    print(x)


addEmployee("raj","parth",x="jay",y ="james")    
    

def test(*args,**kwargs):
    print(args)
    print(kwargs)
    print(args," ",kwargs)


test("raj","parth",x="jay",y ="james")    
    
    

    