#function defination : function is a block of code which is used to perform a specific task
#reuseability of code

# ----------
#50 lines -->
#function solves boiler plate code problem
# boiler plate code --> code which is repeated again and again
#type of function -> UDF PR BUILT IN FUNCTION
# with return type and without parameter
# with return type and with parameter
# without return type and without parameter
# without return type and with parameter

#int sum()
#void sum()
#float sum()

#def keyword is used to define a function
def test():
    print("test function called....")
    print("with return type and without parameter / argument")


test() #function call    

def sum(a,b):
    print("with return type and with parameter / argument")
    return a+b


ans = sum(10,20)
print("sum is",ans)

ans1 = sum(10.20,20.30)
print("sum is",ans1)
print(type(ans1))
    
