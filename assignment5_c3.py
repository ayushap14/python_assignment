class Student:
    def __init__(self):
        self.__name = ""
        self.__rollNumber = ""
    
    def getName(self):
        return self.__name
    
    def setName(self, name):
        self.__name = name
    
    def getRollNumber(self):
        return self.__rollNumber
    
    def setRollNumber(self, rollNumber):
        self.__rollNumber = rollNumber

student = Student()
student.setName("Ayush Parekh")
student.setRollNumber("12345")

print("Name:", student.getName())
print("Roll number:", student.getRollNumber())
