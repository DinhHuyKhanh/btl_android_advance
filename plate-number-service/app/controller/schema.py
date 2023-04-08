from pydantic import BaseModel, validator
from datetime import date
from decimal import Decimal

class UserSchema(BaseModel):
  full_name : str
  email : str

class UserUpdateSchema(BaseModel):
  full_name : str
  email : str

class UserRegister(BaseModel):
  FullName: str
  PhoneNumber: str
  Email: str
  Password: str
  PersonalNumber: str = None
  Address: str = None
  activate: bool = True
  Coin: Decimal = 0
  BirthDay: date = date.today()

class UserLogin(BaseModel):
  email: str
  password: str

