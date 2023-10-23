#kwargs

def getData(x,**kwargs):
    print(kwargs)
    print(type(kwargs))
    
    print(x)
    

getData("am",name="raj",email="raj@gmail.com",age=23)    

