def printStar(func):
    
    def inner():
        print("****")
        func()
    
    
    return inner


def printHash(func):
    def inner():
        print("#####")    
        func()
    
    
    return inner    


@printStar
@printHash
def printData():
    print("hello")


printData()    