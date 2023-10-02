users = [{"id":1,"name":"raj","age":23,"income":20000},{"id":2,"name":"ram","age":25,"income":34000}]

print(users)
users[0]["age"] = 24
print(users)

incometotal = 0

for i in users:
    incometotal = incometotal + i["income"]

print("total income = ",incometotal)