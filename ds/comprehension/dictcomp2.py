players = {"messi":10,"ronaldo":11,"neymar":6,"mbappe":5}
players1 ={}

#"messi":10,"ronaldo":11,"neymar":6,"mbappe":5
for i,j in players.items():
    # 10>=7
    # 11>=7
    # 6>=7
    
    if j >=7:
        #players1["messi"]=10
        #players1["ronaldo"]=11
        players1[i]=j


print(players1)

#comprehension
players2 = {i:j for i,j in players.items() if j>=7}
print(players2)



x = [[10,20],[20,30],[30,20]]

# for i in x: #0 1
#     for j in i:
#         print(j,end=" ")
#     print()    


for i ,j in x:
    print(i," - ",j)        