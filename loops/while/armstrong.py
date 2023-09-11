#153 --> 1 + 125 + 27
#1634 --> 1 + 1296 + 81 + 256 = 
no = int(input("etner no"))
temp = no
temp1 = no
rem =0
sum =0 
nodigit =0

# 153 > 0  TRUE
# 15 >0 TRUE
# 1 >0 TRUE
# 0 >0 FALSE
while temp1>0:
    nodigit+=1 # nodigit = nodigit +1 ,nodigit =2, nodigit =3
    temp1= temp1 //10 # 153 // 10 = 15, 15 // 10 = 1, 1 // 10 = 0
    
    

while no>0:
    rem = no % 10
    #sum = sum + rem**3
    sum = sum + rem**nodigit
    no = no // 10

if temp == sum:
    print("its armstrong..")  
else:
    print("not armstrong..")    
    