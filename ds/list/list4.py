data = ["raj",True,1,1.2,"amit","jay",1000,90.90]

print(data)

#data.sort()
#data.reverse()
data.append("sita")
data.extend(["ram","shyam"])
data.remove(True)

print("after----------")
for i in data:
    print(i)


x = max(data)
print("max===>",x)