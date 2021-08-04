#1.
#class Student:
#    def __init__(self):
#        self.name = "Rolf"
 #       self.grades = (90, 80, 78, 94, 55)

#student = Student()
#print(student.name)
#print(student.grades)


#2.
#class Student:
#    def __init__(self):
#        self.name = "Rolf"
#        self.grades = (90, 80, 78, 94, 55)

#    def average(self):
#        return sum(self.grades) / len(self.grades)

#student = Student()
#print(student.average())         =      #print(Student.average(student))


#3
#class Student:
#    def __init__(self, name):
#        self.name = name
#       self.grades = (90, 80, 78, 94, 55)

#    def average(self):
#        return sum(self.grades) / len(self.grades)

#student = Student("Bob")
#print(student.name)
#print(student.average())



#4.
class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average_grade(self):
        return sum(self.grades) / len(self.grades)

student = Student("Bob", (100, 70, 78, 94, 55))
student2 = Student("Rolf", (90, 80, 78, 94, 55))

print(student.name)
print(student.average_grade())
print(Student.average_grade(student2))   # print(student2.average_grade())