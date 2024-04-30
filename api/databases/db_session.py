from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class DBSession(Base):
    __tablename__ = 'sessions'

    id = Column(Integer, primary_key=True, index=True)
    token = Column(String, unique=True)
    user_id = Column(Integer, index=True)
    created_at = Column(DateTime, index=True)
    expiration = Column(DateTime, index=True)