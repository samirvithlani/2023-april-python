#map --> when you want to manuplate data ---> list
#["10"]


lang = ["hindi","english","tamil","telugu","malayalam"]
#fillang = [i.upper() for i in lang]

# for i in lang:
#     fillang.append(i.upper())

#using map
filllang  = list(map(lambda i : i.upper(),lang))
print(filllang)
print(type(filllang))

marks = [10,21,30,41,50]
#com
markssq = [i **2 for i in marks]
print(markssq)

markssq2 = list(map(lambda i : i **2,marks))
print(markssq2)

#if else with map and lambda
markssq3 = list(map(lambda i : i **2 if i %2 ==0 else i **3,marks))
print(markssq3)



users = ["amit","raj","shyam","ram","mohan","roham","soham"]
#len --> 4 upper case...  title case...

#filusers = [i.upper()  for i in users if len(i) > 4]
filusers = list(map(lambda i : i.upper() if len(i)>4 else i.title(),users))
print(filusers)


x =  [1,2,3,4,5]
# [1,3,5,7,9]
x1 = list(map(lambda i: i + i + 1,x))
print(x1)


data= ["a","b","c","d","e"]


#data = list(map(lambda i: i | i+1,data))
print(data)
