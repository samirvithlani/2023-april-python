from GetterSetterdDemo import StudentModel

class StudetApp:
    
    def getStudentData(self):
        s = StudentModel()
        name = input("Enter Student Name: ")
        s.setStudentName(name)
        age = int(input("Enter Student Age: "))
        s.setStudentAge(age)
        marks = int(input("Enter Student Marks: "))
        s.setStudentMarks(marks)
    
    def printStudentData(self):
        s = StudentModel()
        name = s.getStudentName()
        age = s.getStudentAge()
        marks = s.getStudentMarks()    
        
        print("Student Name: ", name)
        print("Student Age: ", age)
        print("Student Marks: ", marks)



stuapp = StudetApp()
stuapp.getStudentData()
stuapp.printStudentData()        
        
        