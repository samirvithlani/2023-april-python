def isValid(name):
    name  = name.strip()
    if name.startswith('s') and len(name) >3:
        print("name is",name)
        print(len(name))
        return True
    
    return False


if isValid("sachin"):
    print("valid name")
else:
    print("invalid name")    