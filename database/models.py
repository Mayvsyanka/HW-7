from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from .db import Base



class Groups (Base):

    __tablename__ = "Groups"

    id = Column(Integer, primary_key=True, autoincrement=True)
    group_name = Column(String(50), nullable=False)


class Teachers (Base):

    __tablename__ = "Teachers"

    id = Column(Integer, primary_key=True, autoincrement=True)
    teacher_name = Column(String(100), nullable=False)


class Students(Base):
    
    __tablename__ = "Students"

    id = Column(Integer, primary_key=True, autoincrement=True)
    student_name = Column(String(50), nullable=False)
    group_id = Column(Integer, ForeignKey('Groups.id'))


class Subjects(Base):

    __tablename__ = "Subjects"

    id = Column(Integer, primary_key=True, autoincrement=True)
    subject = Column(String(50), nullable=False)
    teachers_id = Column(Integer, ForeignKey('Teachers.id'))


class Marks(Base):

    __tablename__ = "Marks"

    id = Column(Integer, primary_key=True, autoincrement=True)
    mark = Column(Integer, nullable=False)
    day = Column(Date, nullable=False)
    student_id = Column(Integer, ForeignKey('Students.id'))
    subject_id = Column(Integer, ForeignKey('Subjects.id'))


