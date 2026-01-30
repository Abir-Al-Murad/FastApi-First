from fastapi import FastAPI,HTTPException,status,Response,Depends
from pydantic import BaseModel,HttpUrl  #for data validation and data model
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from . import models,utils
from sqlalchemy.orm import Session
from . database import engine, get_db
from . import schemas
from typing import List

app = FastAPI()

models.Base.metadata.create_all(bind=engine)



    
while True:
    try:
        conn = psycopg2.connect(host='localhost',database='sohojx',user='postgres',password='1234',cursor_factory=RealDictCursor)
        
        cursor = conn.cursor()
        print("Successfully connected databse")
        break
    except Exception as e :
        print("Database connection failed")
        print("Error",e)
        time.sleep(2)
        
        
# @app.post("/post")
# def create_post(post: Course):
#     cursor.execute(
#     """
#     INSERT INTO course (name, instructor, duration, website)
#     VALUES (%s, %s, %s, %s) Returning *
#     """,
#     (post.name, post.instructor, post.duration, str(post.website)))
#     new_post = cursor.fetchone()
#     conn.commit()  #commit na korle database e save hobe na.
#     return {"data":new_post}

@app.post("/courses",response_model= schemas.CourseResponse)
def create_course(course:schemas.CourseCreate,db: Session = Depends(get_db)):
    # new_course = models.Course(
    #     name = course.name,
    #     instructor = course.instructor,
    #     duration = course.duration,
    #     website = str(course.website),   #HTTP ache but string kore nite hobe, otherwise erro ashbe
    # )
    new_course = models.Course(**course.model_dump())
    new_course.website = str(new_course.website)

    db.add(new_course)
    db.commit()
    db.refresh(new_course)
    return new_course


@app.get("/")      #decorator

# def aiquest():
#     cursor.execute("""Select * from course""")
#     data = cursor.fetchall()
#     return {"data":data}

@app.get("/courses",response_model= List[schemas.CourseResponse])
def get_course(db: Session = Depends(get_db)):
    course = db.query(models.Course).all()
    return course


# @app.get("/course/{id}")
# def get_course(id:int):
#     cursor.execute('''select * from course where id =%s''',(str(id)))
#     course = cursor.fetchone()
#     if not course:
#         raise HTTPException(
#             status_code= status.HTTP_404_NOT_FOUND,
#             detail = f"Course with id:{id} was not found"
#         )
#     return{"Course_detail":course}


@app.get("/courseNewSystem/{id}",response_model=schemas.CourseResponse)
def get_course(id:int,db: Session = Depends(get_db)):
    course = db.query(models.Course).filter(models.Course.id == id).first()
    if not course:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail= f"Course with id:{id} was not found"
        )
    return course


# @app.delete("/course/{id}",status_code= status.HTTP_204_NO_CONTENT)
# def delete_course(id:int):
#     cursor.execute('''delete from course where id = %s returning *''',(id,))
#     deleted_course = cursor.fetchone()
#     conn.commit()
#     if deleted_course is None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"course with id: {id} doest not exist")
#     return Response(status_code=status.HTTP_204_NO_CONTENT)



@app.delete("/course/sqlAlchemy/delete/{id}",status_code= status.HTTP_204_NO_CONTENT)
def delete_course_sqlAlchemy(id:int,db:Session = Depends(get_db)):
    course_query = db.query(models.Course).filter(models.Course.id == id)
    course = course_query.first()
    if not course:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"course with id: {id} doest not exists")
    course_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


    





# @app.put("/course/{id}")
# def update_course(id:int,course: schemas.CourseCreate):
#     cursor.execute('''Update course set name = %s, instructor =%s,duration=%s,website=%s where id=%s Returning*''',(course.name,course.instructor,course.duration,str(course.website),str(id)))
#     updated_course = cursor.fetchone()
#     conn.commit()
#     if updated_course == None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"course with id:{id} doesn't exists")
#     return {"data":updated_course}

@app.put("/courseNewSystem/{id}",response_model=schemas.CourseResponse)
def update_course(id:int,updated_course:schemas.CourseCreate,db: Session=Depends(get_db)):
    course_query = db.query(models.Course).filter(models.Course.id == id)
    course = course_query.first()
    if not course:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"course with id:{id} does not exist")
    update_data = updated_course.model_dump()
    update_data['website'] = str(update_data['website'])
    course_query.update(update_data,synchronize_session=False) #synchronize_session=False mane holo amra jani je amra kon gulo field update korbo
    db.commit()
    db.refresh(course)
    return course
    

@app.get("/coursealchemy")
def course(db:Session = Depends(get_db)):
    return {"status":"sqlalchemy ORM working"}


@app.post("/users",status_code=status.HTTP_201_CREATED,response_model=schemas.UserResponse)
def create_account(user:schemas.UserCreate,db:Session=Depends(get_db)):
    if db.query(models.User).filter(models.User.email == user.email).first():
        raise HTTPException(400,"Email already exists")
    hashed_password = utils.hash_password(user.password)
    user.password = hashed_password
    new_user = models.User(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
