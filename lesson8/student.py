class Student:
    school_name = "digital school"

    def __init__(self, name, age, course):
        self.name=name
        self.age=age
        self.course=course

student1 = Student("melina", 17, "Python")
student2 = Student("Festa", 20, "Javascript")

print(student1.course)
print(student2.course)