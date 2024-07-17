from pydantic import BaseModel
from sqlalchemy import Column, String, Integer, Boolean
from database import Base

# SQLAlchemy model for Person
class Person(Base):
    __tablename__ = 'customer'
    customer_id = Column(String(40), primary_key=True)
    customer_name = Column(String(40), nullable=False)
    segment = Column(String(40), nullable=False)
    age = Column(Integer, nullable=False)
    country = Column(String(40), nullable=False)
    city = Column(String(40), nullable=False)
    state = Column(String(40), nullable=False)
    postal_code = Column(Integer, nullable=False)
    region = Column(String(40), nullable=False)


