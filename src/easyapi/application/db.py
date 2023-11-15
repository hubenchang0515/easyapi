from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from .config import *

engine = create_engine(SQLALCHEMY_DATABASE_URL)

class BaseModel(DeclarativeBase):
    pass