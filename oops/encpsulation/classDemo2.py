# from  classDemo3 import Test
# from classDemo3 import Test2

from classDemo3 import *

class Department:
    
    def getDept(self):
        print("I am in getDept")


class Employees:
    
    def getEmployeeData(self,name,age):
        print("Name of Employee is",name)
        print("Age of Employee is",age)
        

    def display(self):
        #self.getEmployeeData("Raj",25)
        name = input("Enter name of Employee")
        age = int(input("Enter age of Employee"))
        self.getEmployeeData(name,age)
        dept = Department()
        dept.getDept()
        t = Test()
        t.test()




e = Employees()
e.display()    





        