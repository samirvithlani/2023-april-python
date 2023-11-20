def sumOfDigit(i):
    
    
    for a in  str(i) :
        print('Digit is :',a)
        if int(a)%2==0:
            return True
        else:
            return False
     
    
    
data=[9876,4599,2156,1564,1122,3355]
#data
#x = list(filter(lambda i : condition | true} false,data))
x = list(filter(lambda i : sumOfDigit(i),data))
print('Filtered Data is :',x)



#["ram sita","ramsita",""]