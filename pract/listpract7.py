
users =[]
choice =-1

while True:
    name = input("Enter name :") #krunal #90
    choice =int(input("Enter 1 to add more users or 0 to exit :")) # 1
    if choice ==0:
        users.append(name)
        break
    elif choice ==1:
        users.append(name)
        continue
    else:
        print("Invalid choice")
        break
        
    

print(users)    