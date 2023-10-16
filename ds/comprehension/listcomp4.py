data = [1,"jay","amit",True,3.14,"parth",False,True,2000,"janvi"]

upperdata = [i.upper()  for i  in data if type(i)==str]
print(upperdata)
