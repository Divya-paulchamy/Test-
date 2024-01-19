class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def display(self):
        print("Student Information:")
        print("Name:", self.name)
        print("Grade:", self.grade)
        print("Age:", self.age)

class School(Student):
    def __init__(self, name, grade, age, school_name):
        super().__init__(name, grade, age)
        self.school_name = school_name

    def school_student_display(self):
        print("School Student Information:")
        print("Name:", self.name)
        print("Grade:", self.grade)
        print("Age:", self.age)
        print("School:", self.school_name)

student_obj = Student("John", "10th", 16)
student_obj.display()
print("\n")

school_student_obj = School("Alice", "8th", 14, "XYZ School")

school_student_obj.school_student_display()