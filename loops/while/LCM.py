# 3 4 LCM --> 12

x = 60
y = 75
greater = 0
lcm = 0

# 3 >4  FALSE
if x > y:
    greater = x
else:
    greater = y
    #6
     
   
        
while True:
  #  6 % 5 == 0 and 6 % 6 == 0 FALSE
  #  7 % 5 == 0 and 7 % 6 == 0 FALSE
  #  8 % 5 == 0 and 8 % 6 == 0 FALSE
  # 9 % 5 == 0 and 9 % 6 == 0 FALSE
  # 30 5 % 5 == 0 and 30 % 6 == 0 TRUE
    if ((greater % x ==0 )and (greater % y ==0)):
        lcm = greater
        break
    greater += 1 


print(lcm)    
    