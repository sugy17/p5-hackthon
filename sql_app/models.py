from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Student(Base):
    __tablename__ = "student"

    sid = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    passwd = Column(String)
    phone= Column(String)
    email = Column(String)
    access_token=Column(String, index=True)

    #questions = relationship("Question", back_populates="asked_to")


class Teacher(Base):
    __tablename__ = "teacher"

    tid = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    passwd = Column(String)
    phone= Column(String)
    email = Column(String)
    access_token=Column(String, index=True)

    #questions = relationship("Question", back_populates="asked_to")

class Question(Base):
    __tablename__ = "question"

    qid = Column(Integer, primary_key=True, index=True)
    tid = Column(Integer,  ForeignKey("student.sid"), index=True)
    sid = Column(Integer,  ForeignKey("teacher.tid"), index=True)
    question = Column(String)
    qfile = Column(String)
    answer = Column(String)
    afile = Column(String)

    #asked_to= relationship("Teacher", back_populates="questions")
    #asked_from=relationship("Student", back_populates="questions")
