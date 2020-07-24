from sqlalchemy.orm import Session

from . import models

import uuid

def verify_token(db:Session,token):
    if db.query(models.Teacher).filter(models.Teacher.access_token==token).all():
        return True
    elif db.query(models.Student).filter(models.Student.access_token==token).all():
        return True
    else: return False

def get_student_questions(db: Session, sid:int,status:str):
    if status=='ans':
        return db.query(models.Question).filter(models.Question.sid == sid and models.Question.afile!=None or models.Question.answer !=None).all()
    elif status=='unans':
        return db.query(models.Question).filter(models.Question.sid == sid,models.Question.answer==None, models.Question.afile==None).all()
    else:
        return db.query(models.Question).filter(models.Question.sid == sid).all()

def get_teacher_questions(db: Session, tid:int,status:str):
    if status=='ans':
        return db.query(models.Question).filter(models.Question.tid == tid and (""!=models.Question.answer or ""!=models.Question.afile)).all()
    elif status=='unans':
        return db.query(models.Question).filter(models.Question.tid == tid,models.Question.answer=="" and models.Question.afile=="").all()
    else:
        return db.query(models.Question).filter(models.Question.tid == tid).all()

def get_teachers(db: Session):
    return db.query(models.Teacher.tid,models.Teacher.name).all()


def create_student(db: Session,name,email,phone,passwd):
    try:
        if db.query(models.Student.sid).filter(email==models.Student.email,phone==models.Student.phone).all():
            return False
        token=str(uuid.uuid1())
        db_user = models.Student(name=name,email=email,phone=phone,passwd=passwd,access_token=token)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
    except:
        return False
    return token

def create_teacher(db: Session,name,email,phone,passwd ):
    try:
        if db.query(models.Teacher.tid).filter(email==models.Teacher.email,phone==models.Teacher.phone).all():
            return False
        token=str(uuid.uuid1())
        db_user = models.Teacher(name=name,email=email,phone=phone,passwd=passwd,access_token=token)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return token
    except Exception as e:
        print(e)
        return False


def create_question(db: Session, sid,tid,question,qfile):
    db_item = models.Question(sid=sid,tid=tid,question=question,qfile=qfile)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def create_answer(db: Session,qid,answer,afile):
    item=db.query(models.Question).get(qid)
    item.answer=answer
    item.afile=afile
    db.commit()
    db.refresh(item)
    return item
