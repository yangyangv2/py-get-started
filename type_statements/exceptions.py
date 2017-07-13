
student = {
    "name": 'mark',
    "student_id": 1995
}

student['last_name'] = 'lala'

try:
    last_name = student['last_name']
    numbered = 3 + last_name
except KeyError:
    print('cannot find last_name')
except TypeError as error:
    print('I cannot add these two together')
    print(error)
except Exception:
    print('unknown error')

