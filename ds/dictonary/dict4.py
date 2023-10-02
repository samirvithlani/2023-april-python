teams ={1:["virat","rohit","rahul"],2:["dhoni","jadeja","raina"],3:["messi","ronaldo","neymar"]}

print(teams)


teams[1].append("sachin")
teams[3][0] = teams[3][0].upper()

for i,j in  teams.items():
    print(i)
    for k in j:
        print(k,end=" ")
    print()
    print("---------------")    