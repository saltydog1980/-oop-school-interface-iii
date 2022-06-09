from classes.school import School 

school = School('Ridgemont High') 

while True:
    mode = input("""What would you like to do?
Options:
1. List All Students
2. View Individual Student <student_id>
3. Add a Student
4. Remove a Student <student_id>
5. Quit
: """)

    if mode == '1':
        school.list_students()
    elif mode == '2':
        student_id = input('Enter student id:')
        student_string = str(school.find_student_by_id(student_id))
        print(student_string)
    elif mode == '3':
        school.add_student()
    elif mode == '4':
        school.delete_student()
    elif mode == '5':
        break
