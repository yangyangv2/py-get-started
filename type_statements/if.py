True != False

print(int(True))
print(int(False))

print(str(False))

number = 5

if number == 5:
    print('Number is 5')
else:
    print('Number is not 5')

if 5 and 3:
    print('5 and 3 is defined and truthy')

if not (not ( 0 or 3 )):
    print('0 is defined as faulty')

print("bigger" if 0 > 4 else "smaller")

