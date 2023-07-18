from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Date(Base):
    __tablename__ = "dates"
    id=Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    cargo_type = Column(String, unique=True)
    rate = Column(Integer)
    freight_amount = Column(Integer)
