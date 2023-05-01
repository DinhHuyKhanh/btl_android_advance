from datetime import date, datetime
from decimal import Decimal
from datetime import date
from typing import Optional
from pydantic import BaseModel, EmailStr

class UserLogin(BaseModel):
  email: str
  password: str

class UserSchema(BaseModel):
  FullName: str
  PhoneNumber: str
  Email: EmailStr
  Password: str
  PersonalNumber: str
  Address: str
  activate: Optional[bool] = True
  Coin: Decimal
  BirthDay: date

class UpdateUserSchema(BaseModel):
  PhoneNumber: Optional[str]
  Address: Optional[str]
  activate: Optional[bool]

class EmailSchema(BaseModel):
  email: EmailStr

class ResetPasswordSchema(BaseModel):
  reset_password_token: str
  new_password: str

class UpdatePasswordSchema(BaseModel):
  old_password: str
  new_password: str

class AddMoneySchema(BaseModel):
  money: Decimal

class GateHistorySchema(BaseModel):
  UserId: int
  NumberPlate: str
  CheckInDate: Optional[datetime] = datetime.now()
  CheckOutDate: Optional[datetime] = datetime.now()

class ImageRequest(BaseModel):
  ImagePath: str
