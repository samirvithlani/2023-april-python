marks =[10,20,30]
marks = [[1,2],[3,4],[4,5]]

marks1=[]

# for i in marks:
#     #print(i)
#     for j in i:
#         marks1.append(j)

# print(marks1)        

        
#convert with map        
#marks1 = list(map(lambda i : map(lambda j: j,i),marks))
# marks1 = list(map(lambda i : list(map(lambda j: j,i)),marks))
# print(marks1)

data=[[1,2],[2,3]]
m1=list(map(lambda i: i[0]+i[1],data))
print(m1)

#nested map.. for 2d list
marks1 = list(map(lambda i : list(map(lambda j: j,i)),marks))
print(marks1)

#[1,2],[3,4],[4,5]
#marks1 = list(map(lambda i : i,marks))
#print(marks1)