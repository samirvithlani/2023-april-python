#123 
#123 % 10 = 3
#123 // 10 => 12

#12 % 10 -> 2
#12 //10 ->1

#1  % 10 = 1
#1 // 1044

#432 =9 
no = int(input("enter no"))
sum =0
rem =0
# 432 >0 TRUE
# 43 >0 TRUE
# 4 >0 TRUE
# 0>0 False
while(no>0):
    #rem = 432 % 10 = 2
    # rem = 43 % 10 = 3
    # rem = 4 % 10 -> 4
    rem = no % 10
    #0 = 0 + 2 sum =2
    #2 = 2 + 3 sum =5
    #5 = 5 + 4 sum =9
    sum = sum + rem
    #no = 432 // 10 -> 43
    #no = 43 // 10 -> 4
    #no = 4  //10 -->0
    no = no // 10
    

print("sum of digit  = ",sum)    
    
    