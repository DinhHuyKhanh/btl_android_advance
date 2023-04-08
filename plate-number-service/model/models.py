from sqlalchemy import Boolean, Column, DECIMAL, Integer, String, DateTime
from sqlalchemy.sql import func
from model.database import Base

class UserData(Base):
  __tablename__ = 'user_data'

  Id = Column(Integer, primary_key=True, index=True, autoincrement=True)
  FullName = Column(String(255), nullable=False)
  PhoneNumber = Column(String(255), nullable=False)
  Email = Column(String(255), nullable=False)
  Password = Column(String(255), nullable=False)
  PersonalNumber = Column(String(255), unique=True, nullable=True)
  Address = Column(String(255), nullable=True)
  activate = Column(Boolean, default=True)
  Coin = Column(DECIMAL(10,2), default=0)
  BirthDay = Column(DateTime, server_default=func.now(), nullable=True)
