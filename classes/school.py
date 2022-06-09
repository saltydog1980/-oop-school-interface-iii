from classes.staff import Staff
from classes.student import Student
import os
import csv

class School:
    def __init__(self, name):
        self.name = name
        self.staff = Staff.objects()
        self.students = Student.objects()


    def list_students(self):
        print('\n')
        for i, student in enumerate(self.students):
            print(f'{i + 1}. {student.name} {student.school_id}')
        print('\n')

    def find_student_by_id(self, student_id):
        for student in self.students:
            if student.school_id == student_id:
                return student 
    
    def add_student(self):
        student_data = {'role':'Student'}
        student_data['name']      = input('Enter student name:\n')
        student_data['age']       = input('Enter student age: \n')
        student_data['school_id'] = input('Enter student school id: \n')
        student_data['password']  = input('Enter student password: \n')
        
        self.students.append(Student(**student_data))

        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/students.csv")
        fieldnames = ['name', 'age', 'role', 'school_id', 'password']
        
        with open(path, mode='a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames)
            
            writer.writerow(student_data)

    def delete_student(self):
        school_id = input('Enter student school id: \n')
        student = School.find_student_by_id(self, school_id)
        self.students.remove(student)

        keep_list = []
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, f"../data/students.csv")

        with open(path) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['school_id'] == school_id:
                    pass
                else:
                    keep_list.append(row)
        
        with open (path, mode='w', newline='') as csvfile:
            fieldnames = ['name', 'age', 'role', 'school_id', 'password']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(keep_list)
