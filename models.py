from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from database import engine, SessionLocal

Base = declarative_base()
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float
from database import engine, SessionLocal

Base = declarative_base()

class Product(Base):
    __tablename__ = 'products'
    
    id = Column(Integer, primary_key=True, index=True)  # Primary key
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    description = Column(String, nullable=True)  # Optional field