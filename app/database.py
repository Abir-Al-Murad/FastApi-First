from sqlalchemy import create_engine #database er sathe connection create korar jonno
from sqlalchemy.ext.declarative import declarative_base #model class gulo base class create korbe
from sqlalchemy.orm import sessionmaker

SQLAlCHEMY_DATABASE_URL = 'postgresql://postgres:1234@localhost/sohojx'  #postgresql:username:password@servername/databasename

engine = create_engine(SQLAlCHEMY_DATABASE_URL)
SesssionLocal = sessionmaker(autocommit =False,autoflush= False,bind=engine)

Base = declarative_base()

def get_db():
    db = SesssionLocal()
    try:
        yield db
    finally:
        db.close()
