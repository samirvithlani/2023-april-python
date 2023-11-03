#reduce will produce a single result
#address = ["a","704","cg road","ahmedabad"]
#marks =[10,20,30,40,50]

import functools

marks = [10,20,30,40,50]
# x =10 , y =20
# x 30 , y =30
# x = 60 , y =40
# x = 100 , y =50
#add = functools.reduce(lambda x,y:x+y,marks)
add = functools.reduce(lambda x,y:x+1,marks)
print(add)

average = functools.reduce(lambda x,y:x+y,marks)//len(marks)
print(average)
  
