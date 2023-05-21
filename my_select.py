from sqlalchemy import func, desc, select

from database.models import Teachers, Students, Subjects, Groups, Marks
from database.db import session


def select_1():
    '''
    Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
    '''
    result = session.query(Students.student_name, func.round(func.avg(Marks.mark), 2).label(
        "average_mark")).select_from(Marks).join(Students).group_by(Students.id).order_by(desc('average_mark')).limit(5).all()

    print(result)

def select_2(subj_id):
    '''
    Знайти студента із найвищим середнім балом з певного предмета.
    '''
    result = session.query(Subjects.subject, Students.student_name, func.round(
        func.avg(Marks.mark), 2).label("average_mark")).select_from(Marks).join(Students).join(Subjects).filter(Subjects.id == subj_id).group_by(Students.id, Subjects.subject).order_by(desc('average_mark')).limit(1).all()

    print(result)

def select_3(subj_id):
    '''
    Знайти середній бал у групах з певного предмета.
    '''
    result = session.query(Subjects.subject, Groups.group_name, func.round(
        func.avg(Marks.mark), 2).label("average_mark")).select_from(Marks).join(Students).join(Groups).join(Subjects).filter(Subjects.id == subj_id).group_by(Groups.group_name, Subjects.subject).order_by(desc('average_mark')).all()

    print(result)



def select_4():
    '''
    Знайти середній бал на потоці (по всій таблиці оцінок).
    '''
    result = session.query(func.round(
        func.avg(Marks.mark), 2).label("average_mark")).all()

    print(result)


def select_5():
    '''
    Знайти які курси читає певний викладач
    '''
    result = session.query(Teachers.teacher_name, Subjects.subject).select_from(
        Teachers).join(Subjects).group_by(Subjects.subject, Teachers.teacher_name).all()

    print(result)


def select_6():
    '''
    Знайти список студентів у певній групі.
    '''
    result = session.query(Groups.group_name, Students.student_name).select_from(Groups).join(Students).group_by(Groups.group_name, Students.student_name).all()

    print(result)

def select_7(id_group, id_subject):
    '''
    Знайти оцінки студентів у окремій групі з певного предмета.
    '''

    result = session.query(Groups.group_name, Subjects.subject, Students.student_name, Marks.mark).select_from(Marks).join(Students).join(Subjects).join(
        Groups).filter(Subjects.id == id_subject, Groups.id == id_group).group_by(Groups.group_name, Subjects.subject, Students.student_name, Marks.mark).all()

    print(result)

def select_8(id_teacher):
    '''
    Знайти середній бал, який ставить певний викладач зі своїх предметів.
    '''
    result = session.query(Subjects.subject, Teachers.teacher_name, func.round(
        func.avg(Marks.mark), 2).label("average_mark")).select_from(Marks).join(Subjects).join(Teachers).filter(Teachers.id == id_teacher).group_by(Teachers.teacher_name, Subjects.subject).all()

    print(result)

def select_9(id_student):
    '''
    Знайти список курсів, які відвідує певний студент.
    '''
    result = session.query(Students.student_name, Subjects.subject).select_from(Marks).join(Students).join(
        Subjects).filter(Students.id == id_student).group_by(Students.student_name, Subjects.subject).all()
    print(result)


def select_10(id_student, id_teacher):
    '''
    Список курсів, які певному студенту читає певний викладач.
    '''
    result = session.query(Students.student_name, Teachers.teacher_name, Subjects.subject).select_from(Marks).join(Students).join(Subjects).join(
        Teachers).filter(Students.id == id_student, Teachers.id == id_teacher).group_by(Students.student_name, Teachers.teacher_name, Subjects.subject).all()
    print(result)

if __name__=="__main__":
    print("-----1-----")
    select_1()
    print("-----2-----")
    select_2(2)
    print("-----3-----")
    select_3(2)
    print("-----4-----")
    select_4()
    print("-----5-----")
    select_5()
    print("-----6-----")
    select_6()
    print("-----7-----")
    select_7(1,2)
    print("-----8-----")
    select_8(1)
    print("-----9-----")
    select_9(1)
    print("-----10-----")
    select_10(1,1)


