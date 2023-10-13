#[]
#()
#{} -->
#set()

data = set({12,22,34,56,122,89,12,145,2002,789})

print(data)
print(type(data))


# for i in data:
#     print(i)

data.update([100,200,30,56])
print(data)

data.add(1000)
print(data)


#remove discard pop clear

# data.remove(10000)
# print("after remove..",data)

# data.discard(10000)
# print("after discard..",data)


removedelm = data.pop()
print("removed element is ",removedelm)

while len(data)>0:
    x = data.pop()
    print(x)

print("data....",data)    



