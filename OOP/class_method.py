class Student:
    total_students = 0

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        Student.total_students += 1

    @classmethod
    def get_total_students(cls):
        """Class method which receives Class as first parameter"""
        return f"Total students present are {cls.total_students}"

Student1 = Student("Zaki", 9)
Student2 = Student("Rauhl", 10)
print(Student.get_total_students())
Student3 = Student("sing", 10)
print(Student.get_total_students())

        