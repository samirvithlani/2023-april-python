city = ["Ahmedabad","Mumbai","Pune","Delhi","Chennai"]
filtcity =[]

for i in city:
    if len(i)>4:
        filtcity.append(i.upper())

print(filtcity)        
        