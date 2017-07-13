student = {
    "name": 'mark',
    "student_id": 1995
}

print(student['name'])

print(student.get('name', 'unknown'))

print(student.get('mid name', 'unknown'))

print(student.keys())

print(student.values())

del student['name']

print(student)