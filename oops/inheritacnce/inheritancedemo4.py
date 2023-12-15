#mutipule inheritance  n parent 1 child....

class Uni:
    
    fees = 10000
    
    def getUniData(self):
        print("getUniData")


class College:
    
    fees = 20000
    
    def getCollegeData(self):
        print("getCollegeData")        



class Student(College,Uni):
    
    def getStudentData(self):
        print("getStudentData")
        print("fees: ", self.fees)   


s = Student()
s.getStudentData()     
s.getCollegeData()
s.getUniData()        
    
