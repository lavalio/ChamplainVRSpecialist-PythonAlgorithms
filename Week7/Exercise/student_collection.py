class Student:
    #id=0
    #name = ""
    #gpa = 0

    #def __init__(self,id,name,gpa):
    def __init__(self, id:int, name:str, gpa:float):
        self.id = id
        self.name = name
        self.gpa = gpa

class StudentClass:
    def __init__(self):
        self.students = []

    def add_student(self, student:Student):
        self.students += [student]

    def get_average_gpa(self):
        sum_gpa =0
        for s in self.students:
            sum_gpa += s.gpa
        return sum_gpa/len(self.students)

math_101 = StudentClass()

s1 = Student(100, "Mary", 2.8)
s2 = Student(200, "Bob", 3.2)
s3 = Student(300, "Brendan", 3.5)

math_101.add_student(s1)
math_101.add_student(s2)
math_101.add_student(s3)

print(math_101.get_average_gpa())