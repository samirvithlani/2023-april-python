x = 8
y = 12
smaller = 0

# 8 > 12 FALSE
if x>y:
    smaller = y

#smaller = 8
else:
    smaller = x
    

for i in range(1,smaller+1):
    # 8 % 1 == 0 and 12 % 1 == 0 FALSE
    # 8 % 2 == 0 and 12 % 2 == 0  TRUE 
    # 8 % 3 == 0 and 12 % 3 == 0 FALSE
    # 8 % 4 == 0 and 12 % 4 == 0 TRUE
    # 8 % 5 == 0 and 12 % 5 == 0 FALSE
    # 8 % 6 == 0 and 12 % 6 == 0 FALSE
    # 8 % 7 == 0 and 12 % 7 == 0 FALSE
    # 8 % 8 == 0 and 12 % 8 == 0 FALSE
    
    if((x%i == 0) and (y%i == 0)):
        hcf = i
        # 2
        # 4


print(hcf)        
    