from typing import Optional
from pydantic import BaseModel, EmailStr

class UserSchema(BaseModel):
  fullName: str
  phoneNumber: str
  email: EmailStr
  password: str
  personalNumber: str
  address: str
  activate: Optional[bool] = True
  coin: float
  birthday: str

class UpdateUserSchema(BaseModel):
  phoneNumber: Optional[str]
  password: Optional[str]
  address: Optional[str]

class EmailSchema(BaseModel):
  email: EmailStr
