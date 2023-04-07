from sqlalchemy.sql.sqltypes import Integer, String
from model.database import Base
from sqlalchemy import DECIMAL, Boolean, Column


class DbUser(Base):
  __tablename__ = 'user_data'
  id = Column(Integer, primary_key=True, index=True)
  fullName = Column(String)
  phoneNumber = Column(String)
  email = Column(String)
  password = Column(String)
  personalNumber = Column(String)
  address = Column(String)
  activate = Column(Boolean)
  coin = Column(DECIMAL)
  birthday =  Column(String)
