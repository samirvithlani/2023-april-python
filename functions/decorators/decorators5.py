#4
def smartDiv(func):
    
    def inner(p,r):
        if b == 0:
            print("Can't divide by zero")
        else:
            func(p,r)
    
    return inner


@smartDiv #3
def calc(a,b): #
    print(a/b)
 
 
a = int(input("Enter a: "))
b = int(input("Enter b: "))
calc(a,b)  #1           
        