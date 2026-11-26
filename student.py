
class Student:
    def __init__(self, name, usn, college, city):
        self.name = name
        self.usn = usn
        self.college = college
        self.city = city

    def display(self):
        print("Student Name:", self.name)
        print("USN:", self.usn)
        print("College:", self.college)
        print("City:", self.city)


s = Student("Chetan", "01FE25BCA001", "ABC College", "Hubli")
s.display()
