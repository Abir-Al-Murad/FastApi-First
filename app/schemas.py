from pydantic import BaseModel, HttpUrl


class Course(BaseModel):
    name: str
    instructor: str
    duration: float
    website: HttpUrl