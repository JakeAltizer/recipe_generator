from sqlalchemy import Column, Integer, String, Date, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class DBIngredient(Base):
    __tablename__ = 'inventory'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    amount = Column(Float)
    unit = Column(String)
    expiry_date = Column(Date)
    storage = Column(String)
    created_at = Column(DateTime)