users = ["raj","jay","amit","sujit","suresh","ram"]

#predicate function true false
filuser = list(filter(lambda x : len(x)>3,users))
print(filuser)

filuser1 = list(filter(lambda x: x.startswith("s"),users))

print(filuser1)

# for i in users:
#     if len(i)>3:
#         filuser.append(i)

# print(filuser)        