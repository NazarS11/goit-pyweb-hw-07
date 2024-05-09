from sqlalchemy.orm import sessionmaker
from datetime import date
from faker import Faker
from random import randint
from connect_db import session

from models import Teacher, Student, Group, Subject, Grade

NUMBER_STUDENTS = 50
NUMBER_GROUPS = 3
NUMBER_TEACHERS = 4
NUMBER_GRADES = 20
NUMBER_SUBJECTS = 8
fake_data = Faker()

def generate_fake_data(number_students, number_teachers, number_subjects) -> tuple():
    fake_students = []
    fake_groups = ['CI-11','CI-12','CI-14']
    fake_subjects = ['Algorithm Theory',
                     'Modern Literature',
                     'Environmental Science',
                     'Quantum Mechanics',
                     'Comparative Politics',
                     'Introduction to Psychology',
                     'Ancient Civilizations',
                     'Microeconomic Theory']
    fake_teachers = []

    for _ in range(number_students):
        fake_students.append(fake_data.name())

    for _ in range(number_teachers):
        fake_teachers.append(fake_data.name())

    return fake_students, fake_teachers, fake_subjects, fake_groups

def prepare_data(students, teachers, subjects, groups) -> tuple():
    for_teachers = []
    for teacher in teachers:
        for_teachers.append(Teacher(name=teacher))

    for_students = []
    for student in students:
        for_students.append(Student(name=student, group_id=randint(1, NUMBER_GROUPS)))

    for_groups = []
    for group in groups:
        for_groups.append(Group(name=group))

    for_subjects = []
    for subject in subjects:
        for_subjects.append(Subject(name=subject, teacher_id=randint(1, NUMBER_TEACHERS)))

    for_grades = []
    for student in range(1, NUMBER_STUDENTS + 1):
        for grade_num in range(1, randint(14, NUMBER_GRADES)):
            random_date = fake_data.date_between(start_date=date(2024, 1, 1), end_date=date(2024, 1, 30))
            for_grades.append(Grade(student_id=student, subject_id=randint(1, NUMBER_SUBJECTS), grade=randint(10, 100), date_received=random_date))

    return for_teachers, for_students, for_groups, for_subjects, for_grades

if __name__ == "__main__":
    
    teachers, students, groups, subjects, grades = prepare_data(*generate_fake_data(NUMBER_STUDENTS, NUMBER_TEACHERS, NUMBER_SUBJECTS))

    session.add_all(teachers)
    session.add_all(groups)
    session.commit()
    session.add_all(students)
    session.add_all(subjects)
    session.commit()
    session.add_all(grades)
    session.commit()
