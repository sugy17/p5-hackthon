## uvicorn sql_app.main:app --host 0.0.0.0 --port 80

i think its not not working https 

# API Routes

### Method (for all routes) = GET

### auth token to be passed in parameter 'auth'

# /teachers

    returns a list of lists -> [int,str]

    eg: [[1,"name1"],[2,"name2"]]

# /teacher/create

 params - name=rushaynth&passwd=hello&email=tmail&phone=9999433434577

 returns auth code,tid

    eg:{"auth":"4fdf7d4c-cdf3-11ea-8e2c-309c236ac1d2","tid":2}

# /student/create

 params - name=rushaynth&passwd=hello&email=tmail&phone=9999433434577

 returns auth code,sid

    eg:{"auth":"4fdf7d4c-cdf3-11ea-8e2c-309c236ac1d2","sid":2}


# /student/ask

params -

    sid=1&tid=1&question=bye&auth=4fdf7d4c-cdf3-11ea-8e2c-309c236ac1d2

returns

    eg:{"qfile":null,"qid":5,"answer":null,"tid":1,"afile":null,"sid":1,"question":"bye"}

# /teacher/answer

params -

    qid=1&answer=working&auth=4fdf7d4c-cdf3-11ea-8e2c-309c236ac1d2

returns -

    eg:{"qfile":null,"qid":1,"answer":"working","tid":1,"afile":null,"sid":1,"question":"hello"}

# /student/questions

params - 
    status:takes values ans,unans,all
        
    sid - student id

returns json with keys -

    sid,tid,qid -> ints

    question,qfile,answer,afile->str


# /teacher/questions

params - 
    status:takes values ans,unans,all
        
    sid : student id

returns json with keys -

    sid,tid,qid -> ints

    question,qfile,answer,afile->str
