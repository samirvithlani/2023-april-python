users = ["amit","ajay","neha","maan","krunal","ajay"]

name = input("enter name to remove : ")
#first check that name is available or not after that remove....

x = users.count(name)
print(x)

if x >0:
    users.remove(name)
else:
    print("name not found...")    

print("after remove...")
print(users)