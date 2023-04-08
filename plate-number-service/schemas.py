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
  address: Optional[str]

class EmailSchema(BaseModel):
  email: EmailStr

class ResetPasswordSchema(BaseModel):
  reset_password_token: str
  old_password: str
  new_password: str

class UpdatePasswordSchema(BaseModel):
  old_password: str
  new_password: str