from sqlalchemy import Column, Float, Integer, Text
from bd.conect_db import Base


class Wanted(Base):
    __tablename__ = "wanted"
    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    sex = Column(Text)
    weight = Column(Float, nullable=True)
    reward_text = Column(Text)
    description = Column(Text)
    images = Column(Text)
    place_of_birth = Column(Text)
    warning_message = Column(Text)
    hair = Column(Text)
    eyes = Column(Text)
    race = Column(Text)
    occupation = Column(Text)
