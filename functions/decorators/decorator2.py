def isLogin(func):
    
    def inner():
        print("I am checking that user is login or Not:")
        print("I am if block | if user is login i am calling func() else i will return from here only..")
        func() #usersList()
    
    return inner


@isLogin
def usersList():
    print("I am usersList function")    
    

usersList()    
        