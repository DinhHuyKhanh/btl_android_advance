from pydantic import BaseModel

class UserSchema(BaseModel):
  full_name : str
  email : str

class UserUpdateSchema(BaseModel):
  full_name : str
  email : str
