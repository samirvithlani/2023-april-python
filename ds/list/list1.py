#empty list
#users = []
users = ["raj","jay","parth"]
print("users===>",users)
print(type(users))
l = len(users)
print("length of list===>",l)
# print(users[0])
# print(users[1])
# print(users[2])

#0 ,3
# for i in range(len(users)):
#     print(users[i])


users.append("raj")
users.extend(["ram","sita","sneh","raj"])

users[0]="Raj"

#insert

users.insert(1,"shyam")

#removing....

#overloaded function....
removedelm1 = users.pop()
removedelm2 = users.pop(2)
print("removing    => ",removedelm1)
print("removing    => ",removedelm2)


#users.remove("parth")


users.sort()


for i in users:
    print(i)


m = max(users)
print("max===>",m)