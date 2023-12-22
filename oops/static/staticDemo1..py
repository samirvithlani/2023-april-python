class Test:
    
    
    def __init__(self):
        self.x = 10 # instance variable
        self.y = 20 # instance variable


#userName = "raj"
#r1.userName = "raj"
#r2.userName = "rajvi"
#facebook --> userName -->

#uni ---> NameOfUni --> common ==> single copy --> static variable

t1 = Test()
t2 = Test()

# t1.x = 888
# t1.y = 999

# t2.x = 777
# t2.y = 666

print(t1.x, t1.y)
print(t2.x, t2.y)
        
    