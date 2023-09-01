#0 1 1 2 3 5 8...

a= 0
b =1
print(a)
print(b)
sum = a + b
for i in range(1,10):
    print(sum,end=" ")  #1 ,2 3 5
    
    a = b # a =1 , a =1 , a = 2
    b = sum # b = 1 , b = 2 , b =3
    sum = a + b # sum = 2 , sum = 3,sum = 5
    