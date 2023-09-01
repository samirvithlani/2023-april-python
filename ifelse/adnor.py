#and or 
# if(no% 2 ==0 and no>-50):
#  t        t      t
#  f        -      f
#  t       f      f

#or
# f      f     f
#f       t    t
#t      -      t

no = int(input("Enter no: "))

if (no % 2 ==0 or no >= 50) and (no % 3 ==0):
    print("True")

else:
    print("False")    