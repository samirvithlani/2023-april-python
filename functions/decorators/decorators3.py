

def eligible(func):
    score = 242
    def inner():
        if score >241:
            print("You are eligible for the tournament")
            func()
        else:
            print("You are not eligible for the tournament")
    
    return inner            


@eligible
def getTrophy():
    print("You got a trophy!")


getTrophy()    