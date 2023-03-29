from sqlalchemy.sql.sqltypes import Integer, String
from model.database import Base
from sqlalchemy import Boolean, Column, DECIMAL


class DbUser(Base):
  __tablename__ = 'users'
  id = Column(Integer, primary_key=True, index=True)
  phone_number = Column(String)
  email = Column(String)
  password = Column(String)
  personal_number = Column(String)
  address = Column(String)
  activate = Column(Boolean)
  personal_number = Column(String)
  coin = Column(DECIMAL)
  birth_day =  Column(String)

