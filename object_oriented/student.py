students = []

class Student:

    # class attribute (static variable)
    school_name = 'springfield elementary'

    # constructor
    def __init__(self, name, student_id=332):
        self.name = name
        self.student_id = student_id
        students.append(self)

    # to_string
    def __str__(self):
        return "Student " + self.name

    def get_name_capitalize(self):
        return self.name.capitalize()

    def get_school_name(self):
        return self.school_name