def isValid(data):
    try:
        if " " in data:
            raise ValueError("No spaces allowed")
        if len(data) < 8:
            raise ValueError("Length should be atleast 8")
        
    except ValueError as e:
        print(e)    


isValid("hello world")    


name = "hello world"
print(name.isspace())