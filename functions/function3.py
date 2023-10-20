# #name starts '' and length is 3
# def isValid(name):
#     if name.startswith('s') and len(name) >3:
#         return True
    
#     return False

# x = isValid("sac   ")
# print(x)



#name starts '' and length is 3
def isValid(name):
    name  = name.strip()
    if name.startswith('s') and len(name) >3:
        print("name is",name)
        print(len(name))
        return True
    
    return False

x = isValid("sachin")
print(x)


