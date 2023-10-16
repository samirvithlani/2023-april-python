data = [1,"jay","amit",True,3.14,"parth",False,True,2000]
strdata = []

for i in data:
    if type(i)==str:
        strdata.append(i)

print(strdata)        

strdata1 =[i for i in data if type(i)==str]
print(strdata1)