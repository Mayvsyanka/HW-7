from datetime import date, datetime, timedelta
from faker import Faker
from random import randint, choice
from sqlalchemy import select
from colorama import Style

from database.db import session
from database.models import Teachers, Students, Subjects, Groups, Marks

def study_days(start: date, end: date):
    result = []
    current_date = start
    while current_date <= end:
        if current_date.isoweekday()<6:
            result.append(current_date)
        current_date += timedelta(1)
    return(result)

def append_data():

    subjects = ["math", "physics", "chemistry", "English", "history"]

    groups = ["PM-1", "PM-2", "PM-3"]

    fake = Faker()

    num_teachers = 5

    num_students = 40

    def add_teachers():
        for i in range(num_teachers):
            teacher = Teachers(teacher_name = fake.name())
            session.add(teacher)
        session.commit()
    
    def add_subjects():
        teachers = session.scalars(select(Teachers.id)).all()
        for sub in subjects:
            session.add(Subjects(subject = sub, teachers_id = choice(teachers)))
        session.commit()

    def add_groups():
        for group in groups:
            session.add(Groups(group_name=group))
        session.commit()

    def add_students():
        gr_identify = session.scalars(select(Groups.id)).all()
        for i in range(num_students):
            student = Students(student_name = fake.name(), group_id = choice(gr_identify))
            session.add(student)
        session.commit()

    def add_marks():
        start_date = datetime.strptime('2022-09-01', '%Y-%m-%d')

        end_date = datetime.strptime('2023-05-30', '%Y-%m-%d')
        
        range_date = study_days(start=start_date, end=end_date)

        sub_identify = session.scalars(select(Subjects.id)).all()

        st_identify = session.scalars(select(Students.id)).all()

        for d in range_date:
            id_subject = choice(sub_identify)
            random_id_student = [choice(st_identify) for _ in range(5)]

            for id in random_id_student:
                mark = Marks(mark=randint(1, 5), day = d, student_id = id, subject_id = id_subject,)
                session.add(mark)
        session.commit()

    add_teachers()
    add_groups()
    add_subjects()
    add_students()
    add_marks()

if __name__ == "__main__":
    append_data()