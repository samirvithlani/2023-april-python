data = [11,22,10,22,30,40,60,45,30]
uniquelist = []
duplist = []
#i =11,22,10,22,30,30

for i in data:
    # 11 not in uniquelist True
    # 22 not in uniquelist True
    # 10 not in uniquelist True
    # 22 not in uniquelist False
    # 33 not in uniquelist True
    if i not in uniquelist:
        uniquelist.append(i)#11,22,30
    else:
        duplist.append(i)#22,30
            

print(uniquelist)     
print(duplist)   
