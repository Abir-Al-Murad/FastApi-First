from pydantic import BaseModel, HttpUrl, EmailStr
from datetime import datetime

#define request body schema

class CourseCreate(BaseModel):
    name: str
    instructor: str
    duration: float
    website: HttpUrl
    
class CourseResponse(CourseCreate):
    id : int
    
    class Config:
        orm_model = True
        
# class CourseResponse(BaseModel):  #Response e only name and instructor dakhabe
#     name:str
#     instructor:str

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    
class UserResponse(BaseModel):
    id:int
    email:EmailStr
    created_at:datetime
    class Config:
        orrm_model = True
        
class UserLogin(BaseModel):
    email : EmailStr
    password:str
    