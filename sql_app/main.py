from typing import List

from fastapi import Depends, FastAPI, HTTPException,Request,Response

from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from . import crud, models
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.middleware("http")
async def authenticate(request: Request, call_next,db: Session = next(get_db())):
    print(str(request.url).split('?')[0].split('/')[-1])
    if str(request.url).split('?')[0].split('/')[-1]!='create':
        try:
            if  not crud.verify_token(db,request.query_params['auth']):
                return Response(status_code=400, content='{details:"unauthorized"}')
        except Exception as e:
            return Response(status_code=400, content='{details:"'+str(e)+'"}')
    response = await call_next(request)
    return response


@app.get("/teacher/create")
async def register_teacher(name,email,phone,passwd,db: Session = Depends(get_db)):
    auth_code=crud.create_teacher(db=db, name=name,email=email,phone=phone,passwd=passwd)
    if not auth_code:
         raise HTTPException(status_code=400, detail="already registered")
    return {"auth":auth_code}

@app.get("/student/create")
async def register_student(name,email,phone,passwd,db: Session = Depends(get_db)):
    auth_code = crud.create_student(db=db, name=name,email=email,phone=phone,passwd=passwd)
    if not auth_code:
         raise HTTPException(status_code=400, detail="already registered")
    return {"auth":auth_code}

@app.get("/student/ask")
async def ask_question(sid,tid,question=None,qfile=None,db: Session = Depends(get_db)):
    return crud.create_question(db=db,sid=sid,tid=tid,question=question,qfile=qfile)

@app.get("/teacher/answer")
async def answer_question(qid,answer=None,afile=None,db: Session = Depends(get_db)):
    return crud.create_answer(db, qid,answer,afile)


@app.get("/student/questions")
async def send_student_questions(status:str,sid:int, db: Session = Depends(get_db)):
    questions = crud.get_student_questions(db, sid=sid,status=status)
    return questions

@app.get("/teacher/questions")
async def send_teacher_questions(status:str,tid:int, db: Session = Depends(get_db)):
    questions = crud.get_teacher_questions(db, tid=tid,status=status)
    return questions

@app.get("/teachers")
async def send_teachers(db: Session = Depends(get_db)):
    teachers = crud.get_teachers(db)
    return teachers
