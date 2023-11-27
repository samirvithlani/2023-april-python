class MyCustomeExcpetion(Exception):
    
    def __init__(self, msg):
        self.msg = msg
        super().__init__(self.msg)



age = int(input("Enter your age: "))

try:
    if age<18:
        raise MyCustomeExcpetion("You are not allowed to vote")
    
    print("Your age is: ", age)
except MyCustomeExcpetion as e:
    print(e)    


        
    
        
        