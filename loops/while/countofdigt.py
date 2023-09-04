no = int(input("enter no : "))

#123 -3
#123 // 10 no = 12, no 12 // 10 = 1 1 // 10 =0
#45677 // 10 4567, 4567 //10  456, 456 //10  45 , 45 //10 4, 4 // 10 0

# 667
count =0
# 667>0 True
# 66>0 True
#6 >0 True
#0>0 FALSE
while(no>0):
# while(no!=0):
    count+=1 # count = count +1  count =1,count =2,count =3
    no = no // 10 # 667 = 667 //10 no = 66, 66 // 10 = no =6, 6 //10 = 0
    
print("no of digits = ",count)
    