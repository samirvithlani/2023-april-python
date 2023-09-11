#123
# 321
no = 121
rem =0
sum =0
temp = no
#12>0 TRUE
#1>0 TRUE
#0>0 FALSE
while no>0:
    #123 % 10 = rem = 3
    #12 % 10 = rem = 2
    #1 % 10 = rem = 1
    rem = no % 10
    #0 *10 + 3 = 3 sum =3
    # 3 * 10 +2 = 32 sum = 32
    #32 * 10 + 1 = 321 sum = 321
    sum = sum * 10 + rem
    #123 // 10 = 12
    #12 // 10 = 1
    #1 // 10 = 0
    no = no //10
   

print("reverse no = ",sum)   

if temp == sum:
    print("palindrome")

else:
    print("not palindrome")     
