from fastapi import FastAPI
# from pydantic import BaseModel,HttpUrl  #for data validation and data model
from . routers import user,course,auth

app = FastAPI()

# models.Base.metadata.create_all(bind=engine)


app.include_router(course.router)
app.include_router(user.router)
app.include_router(auth.router)


    
# while True:
#     try:
#         conn = psycopg2.connect(host='localhost',database='sohojx',user='postgres',password='1234',cursor_factory=RealDictCursor)
        
#         cursor = conn.cursor()
#         print("Successfully connected databse")
#         break
#     except Exception as e :
#         print("Database connection failed")
#         print("Error",e)
#         time.sleep(2)
        
        
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



# @app.get("/")      #decorator

# def aiquest():
#     cursor.execute("""Select * from course""")
#     data = cursor.fetchall()
#     return {"data":data}



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



# @app.delete("/course/{id}",status_code= status.HTTP_204_NO_CONTENT)
# def delete_course(id:int):
#     cursor.execute('''delete from course where id = %s returning *''',(id,))
#     deleted_course = cursor.fetchone()
#     conn.commit()
#     if deleted_course is None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"course with id: {id} doest not exist")
#     return Response(status_code=status.HTTP_204_NO_CONTENT)






    





# @app.put("/course/{id}")
# def update_course(id:int,course: schemas.CourseCreate):
#     cursor.execute('''Update course set name = %s, instructor =%s,duration=%s,website=%s where id=%s Returning*''',(course.name,course.instructor,course.duration,str(course.website),str(id)))
#     updated_course = cursor.fetchone()
#     conn.commit()
#     if updated_course == None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"course with id:{id} doesn't exists")
#     return {"data":updated_course}




