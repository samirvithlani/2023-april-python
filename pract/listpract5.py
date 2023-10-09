#data = [12,22,45,4,3,21,6]
data = [[11,22],[22,33],[33,44]]
#        [11+22,22+33,33+44][33,55,77]
# max = data[0] #max = 12

# for i in data:
#     if i>max:
#         max =i

# print("max = ",max)        

#print(max(data))

ans =0
sumlist = []
for i in data:
    for j in i:
        ans = ans + j
        
    #print(ans,end=" ")
    sumlist.append(ans)
    print()
    ans =0


print(sumlist)    
print(max(sumlist))
        
    