# program to display student's marks from record
student_name = str(input("Enter your name:"))

#data of students stored name as marks
marks = {'Sonjoy': 90, 'Rifat': 55, 'Nafi': 77}

for student in marks:
    if student == student_name:
        print(marks[student])
        break
else:
    print('No entry with that name found.')
