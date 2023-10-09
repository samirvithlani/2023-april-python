#lisy --> data type... 
# array --> list
# array -> static -->
# array is group of similar kind of data...
# list is group heterogeneous data... ["raj", 10, 20.5, True]
#list is mutable..

data = ["raj","jay","ajay","parth"]

print(data)
#after adding new element
data.append("vijay")
data.extend(["amit","rajesh"])
#after extend
data.insert(3,"rahil")
#remove....
print(data)
#removedelm = data.pop()
removedelm = data.pop(2)
print('removing...',removedelm)


#after pop
print("after pop...")
print(data)


#removing data using element

data.remove("parth")
print("after remove...")
print(data)



