from sqlalchemy import Column, Integer, String, Float
from .database import Base
class Sandwich(Base):
    __tablename__ = "sandwiches"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    ingredients = Column(String)
    price = Column(Float)
