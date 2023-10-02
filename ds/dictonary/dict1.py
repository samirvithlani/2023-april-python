#[],(),{},{}

data = {1:"java",2:"python",3:"c",4:"c++",5:"ruby",1:"javaScript",6:"python","name":"python"}
print(data)
print(data[1])
print(data[4])
print(data["name1"])

#dict is mutable
data[4]="cpp"
print(data)

x = data.get(44)
print("x = ",x)



#print(type(data))