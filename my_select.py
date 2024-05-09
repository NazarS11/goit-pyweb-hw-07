from sqlalchemy import func, desc
from models import Teacher, Student, Group, Subject, Grade
from sqlalchemy import select
from connect_db import session

def select_1():
    q = session.query(Student.name, func.round(func.avg(Grade.grade)).label('average_grade'))\
        .select_from(Grade).join(Student).group_by(Student.id).order_by(desc('average_grade')).limit(5).all()
    return q

print(select_1())


def select_2():
    subquery = session.query(Subject.name.label('subject_name'), Student.name.label('student_name'), 
                             func.round(func.avg(Grade.grade)).label('average_grade'))\
                      .select_from(Grade).join(Student).join(Subject).filter(Grade.subject_id == 1)\
                      .group_by(Subject.name, Student.name).subquery()

    q = session.query(subquery.c.subject_name, subquery.c.student_name, subquery.c.average_grade)\
               .order_by(desc(subquery.c.average_grade)).limit(1).all()
    return q

print(select_2())


def select_3():
    subquery = session.query(Subject.name.label('subject_name'), Group.name.label('group_name'), 
                            func.round(func.avg(Grade.grade)).label('average_grade'))\
                    .select_from(Grade).join(Student).join(Subject).join(Group).filter(Grade.subject_id == 1)\
                    .group_by(Subject.name, Group.name).subquery()

    q = session.query(subquery.c.subject_name, subquery.c.group_name, subquery.c.average_grade)\
            .order_by(desc(subquery.c.group_name)).all()
    return q

print(select_3())


def select_4():
    q = session.query(func.round(func.avg(Grade.grade)).label('average_grade')).select_from(Grade).all()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
    return q

print(select_4())


def select_5():
    q = session.query(Teacher.name, Subject.name)\
        .select_from(Subject).join(Teacher).filter(Teacher.id == 3).order_by(Subject.name).all()
    return q

print(select_5())


def select_6():
    q = session.query(Group.name, Student.name)\
        .select_from(Group).join(Student).filter(Group.id == 3).order_by(Student.name).all()
    return q

print(select_6())


def select_7():
    q = session.query(Subject.name, Group.name, Student.name, Grade.grade)\
        .select_from(Grade).join(Subject).join(Student).join(Group).filter(Subject.id == 2).filter(Group.id == 1).order_by(Student.name).all()
    return q

print(select_7())


def select_8():
    q = session.query(Teacher.name, Subject.name, func.round(func.avg(Grade.grade)).label('average_grade'))\
        .select_from(Grade).join(Subject).join(Teacher).filter(Teacher.id == 3).group_by(Subject.id, Teacher.name).order_by(Subject.name).all()
    return q

print(select_8())


def select_9():
    q = session.query(Student.name, Subject.name)\
        .select_from(Grade).join(Student).join(Subject).join(Group).filter(Student.id == 4).group_by(Subject.id, Student.name).order_by(Subject.name).all()
    return q

print(select_9())


def select_10():
    q = session.query(Student.name, Teacher.name, Subject.name)\
        .select_from(Grade).join(Student).join(Subject).join(Group).join(Teacher).filter(Student.id == 4).filter(Teacher.id == 3)\
        .group_by(Subject.id, Teacher.name, Student.name).order_by(Subject.name).all()
    return q

print(select_10())


def select_2_1():
    q = session.query(Student.name, Teacher.name, Subject.name, func.round(func.avg(Grade.grade)).label('average_grade'))\
        .select_from(Grade).join(Student).join(Subject).join(Group).join(Teacher).filter(Student.id == 4).filter(Teacher.id == 3)\
        .group_by(Subject.id, Teacher.name, Student.name).order_by(Subject.name).all()
    return q

print(select_2_1())


def select_2_2():
    subquery = session.query(func.max(Grade.date_received).label("max_date"))\
        .join(Student).join(Subject).join(Group)\
        .filter(Group.id == 1).filter(Subject.id == 1).scalar_subquery()

    q = session.query(Group.name, Subject.name, Student.name, Grade.date_received, Grade.grade)\
        .select_from(Grade)\
        .join(Student).join(Subject).join(Group)\
        .filter(Group.id == 1).filter(Subject.id == 1).filter(Grade.date_received == subquery).all()
    
    return q

print(select_2_2())




