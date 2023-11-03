tech = ["java","python","c","node","javascript","scala","ruby","php","c++","c#"]

techlist = list(filter(lambda x : len(x)>4,tech))
print(techlist)


companies = ["google.inc","tata.ltd","ril.ltd","meta.inc","amazone.inc"]
inccompanies =list(filter(lambda x: x.endswith(".inc"),companies))


# for i in companies:
#     if i.endswith(".inc"):
#         inccompanies.append(i)
        
print(inccompanies)


data =[100,20,34,56,345,67,89,77,12,34,12,18]
data1= list(filter(lambda x:x %2==0 and x % 3 ==0 and x % 4 ==0 ,data))
print(data1)



no = 12
print(type(no))

strno = str(no)
print(type(strno))

#787 ---> 
#20
aadharcardno = [123786,234567,789786,112131]


filad =list(filter(lambda x:str(x).endswith("786"),aadharcardno))
print(filad)

        
