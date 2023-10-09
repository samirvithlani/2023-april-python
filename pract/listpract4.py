a =[[1,2,3],[4,5,6],[7,8,9]]

ans =0
for i in a:
    for j in i:
        print(j,end=" ")
        ans = ans + j
    
    print("ans = ",ans,end="  ")   
    ans =0
    print()    

#print("ans = ",ans)    


# for i in range(0,len(a)):
#     for j in range(0,len(a[i])):
#         print(a[i][j],end=" ")
    
#     print()    