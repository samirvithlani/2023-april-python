try:
    no1 = int(input("enter no 1"))
    no2 = int(input("enter no 2"))
    
    x = no1 / no2
    print("div = ",x)
except ZeroDivisionError:
    print("can not divide by zero..")    
except ValueError:
    print("check your input...")    

except:
    print("somethong went wrong..")    


print("end..")    