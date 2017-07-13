from student import Student

class HighSchoolStudent(Student):
    school_name = 'springfield high school'

    def get_school_name(self):
        return 'this is a high school student'

    def get_name_capitalize(self):
        org_value = super().get_name_capitalize()
        return org_value + ' HS'
