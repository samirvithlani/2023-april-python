class StudentModel:
    
    __name = None
    __age = None
    __marks = None
    
    def setStudentName(self,name):
        self.__name = name
    
    def getStudentName(self):
        return self.__name 
    
    def setStudentAge(self,age):
        self.__age = age
    
    def getStudentAge(self):
        return self.__age
    
    def setStudentMarks(self,marks):
        self.__marks = marks
    
    def getStudentMarks(self):
        return self.__marks        
       
    