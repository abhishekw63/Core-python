'''
'{
    raj':{'roll':25,'gender':'male','dept':'EEE'}
    }
'''
students=dict()
for i in range(4):
    name=input('enter the name:')
    roll=int(input('enter the roll no:'))
    gender=input('enter the gender:')
    dept=input('enter the department:')

    students[name]={'roll_number':roll,'gender':gender,'dept':dept}
print(students)
'''
students = dict()

while True:
    student_data = input("Enter student details (name roll gender dept) or type 'exit' to stop:\n")
    
    if student_data.lower() == 'exit':
        break
    
    details = student_data.split()
    print(details)
    
    if len(details) == 4:
        name, roll, gender, dept = details #unpacking
        students[name] = {'roll_number': int(roll), 'gender': gender, 'dept': dept}

print(students)
'''