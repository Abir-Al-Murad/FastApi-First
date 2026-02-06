from pydantic import BaseModel, HttpUrl, EmailStr
from datetime import datetime
from typing import Optional

#define request body schema

# 👉 Schema = API data contract

# Request body কেমন হবে

# Response এ কী যাবে

# Data validate হবে কিনা


# BaseModel → সব schema এর base

# HttpUrl → valid URL enforce করে

# EmailStr → valid email enforce করে

# Optional → value থাকতে পারে / না-ও থাকতে পারে


class CourseCreate(BaseModel):
    name: str
    instructor: str
    duration: float
    website: HttpUrl
    
class CourseResponse(CourseCreate):   #course field er shob field dekhabe plus id dekhabe
    id : int
    creator_id: int
    class Config:
        orm_mode = True
        
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
        orm_mode = True
        
class UserLogin(BaseModel):
    email : EmailStr
    password:str
    
class Token(BaseModel):
    access_token : str
    token_type : str

class TokenData(BaseModel):
    id: Optional[int]= None