class Library:
    
    def __init__(self,**kwargs):
        print("I am in parameterized constructor")
        print("kwargs is",kwargs)
        



l = Library(name="abc",author="ok",price=100.0,qty=10)
        