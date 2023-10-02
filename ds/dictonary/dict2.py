users = {"name": "John", "age": 30, "city": "New York","isActive":True}

k = users.keys()
print(k)
v = users.values()
print(v)

kv = users.items()
print(kv)



users["name"]="John Snow"
users["house"]="Stark"

#append

users.update({"email":"johnSnow@stark.com","phone":"1234567890","age":23})

for i,j in users.items():
    print(i," = ",j)