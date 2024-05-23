from sqlalchemy import Column, Integer, String, Text, JSON, DateTime, ARRAY
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class DBRecipe(Base):
    __tablename__ = 'recipes'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    prep_time_minutes = Column(Integer)
    cook_time_minutes = Column(Integer)
    total_time_minutes = Column(Integer)
    num_servings = Column(Integer)
    ingredients = Column(ARRAY(JSON))
    instructions = Column(ARRAY(JSON))
    summary = Column(Text)
    credits = Column(ARRAY(Text))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
