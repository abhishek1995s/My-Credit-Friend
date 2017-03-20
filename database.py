import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
Base = declarative_base()
class Webdata(Base):
    __tablename__ = 'webdata'

    id = Column(Integer, primary_key=True)
    bank_name = Column(String(250), nullable=False)
    personal = Column(String(250))
    home = Column(String(250))
    educational = Column(String(250))
    gold = Column(String(250))
engine = create_engine('sqlite:///info.db')


Base.metadata.create_all(engine)
