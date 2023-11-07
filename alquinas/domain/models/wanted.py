from sqlalchemy import Column, Float, Integer, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Wanted(Base):
    __tablename__ = "wanted"
    id = Column(Integer, primary_key=True)
    name = Column(Text, unique=True)
    sex = Column(Text, unique=True)
    weight = Column(Float, nullable=True)
    reward_text = Column(Text, unique=True)
    description = Column(Text, unique=True)
    images = Column(Text, unique=True)
    place_of_birth = Column(Text, unique=True)
    warning_message = Column(Text, unique=True)
    hair = Column(Text, unique=True)
    eyes = Column(Text, unique=True)
    race = Column(Text, unique=True)
    occupation = Column(Text, unique=True)
