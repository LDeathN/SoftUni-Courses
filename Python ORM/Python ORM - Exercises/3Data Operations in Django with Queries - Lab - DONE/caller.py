import os
import django
from datetime import date
from datetime import datetime

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models
from main_app.models import Student
# Create and check models


def add_students():
    students_ids = ["FC5204", "FE0054", "FH2014", "FH2015"]
    first_names = ["John", "Jane", "Alice", "Bob"]
    last_names = ["Doe", "Smith", "Johnson", "Wilson"]
    birth_dates = [datetime.strptime('15/05/1995', '%d/%m/%Y').date(), "null", datetime.strptime('10/02/1998', '%d/%m/%Y').date(), datetime.strptime('25/11/1996', '%d/%m/%Y').date()]
    emails = ["john.doe@university.com", "jane.smith@university.com", "alice.johnson@university.com", "bob.wilson@university.com"]
    for i in range(0, 4):
        if birth_dates[i] == "null":
            student = Student(
                student_id=students_ids[i],
                first_name=first_names[i],
                last_name=last_names[i],
                email=emails[i],
            )
        else:
            student = Student(
                student_id=students_ids[i],
                first_name=first_names[i],
                last_name=last_names[i],
                birth_date=birth_dates[i],
                email=emails[i],
            )
        student.save()


def get_students_info():
    students = Student.objects.all()
    result = ""
    for student in students:
        result += f"Student №{student.student_id}: {student.first_name} {student.last_name}; Email: {student.email}\n"
    return result


def update_students_emails():
    all_students = Student.objects.all()
    for student in all_students:
        new_email = student.email.replace('@university.com', '@uni-students.com')
        student.email = new_email
        student.save()


def truncate_students():
    all_students = Student.objects.all()
    for student in all_students:
        student.delete()

# Run and print your queries



