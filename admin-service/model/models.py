from sqlalchemy import Column, Integer, String, Boolean, DateTime, Float, Enum, ForeignKey
from sqlalchemy.orm import relationship
from model.database import Base

class User(Base):
  __tablename__ = 'Users'
  Id = Column(Integer, primary_key=True)
  FullName = Column(String(255), nullable=False)
  PhoneNumber = Column(String(255), nullable=False)
  Email = Column(String(255), nullable=False)
  Password = Column(String(255), nullable=False)
  PersonalNumber = Column(String(255), unique=True)
  Address = Column(String(255))
  activate = Column(Boolean)
  Coin = Column(Float)
  BirthDay = Column(DateTime)

class Role(Base):
  __tablename__ = 'Role'
  Id = Column(Integer, primary_key=True)
  RoleName = Column(Enum('ADMIN', 'USER'), nullable=False)

class UserHasRoles(Base):
  __tablename__ = 'UserHasRoles'
  roleId = Column(Integer, ForeignKey('Role.Id'), primary_key=True)
  userId = Column(Integer, ForeignKey('Users.Id'), primary_key=True)

class NumberPlate(Base):
  __tablename__ = 'NumberPlate'
  Id = Column(Integer, primary_key=True)
  NumberPlate = Column(String(255), nullable=False)
  ImagePath = Column(String(255))

class UserHasPlates(Base):
  __tablename__ = 'UserHasPlates'
  UserId = Column(Integer, ForeignKey('Users.Id'), primary_key=True)
  NumberPlateId = Column(Integer, ForeignKey('NumberPlate.Id'), primary_key=True)

class TransactionHistory(Base):
  __tablename__ = 'TransactionHistory'
  UserId = Column(Integer, ForeignKey('Users.Id'), primary_key=True)
  Coin = Column(Float)
  CreatedDate = Column(DateTime)
  description = Column(String(255))

class GateHistory(Base):
  __tablename__ = 'GateHistory'
  Id = Column(Integer, primary_key=True)
  UserId = Column(Integer, ForeignKey('Users.Id'), nullable=False)
  NumberPlate = Column(Integer, ForeignKey('NumberPlate.Id'), nullable=False)
  CheckInDate = Column(DateTime)
  CheckOutDate = Column(DateTime)
  ImagePath = Column(String(255))
