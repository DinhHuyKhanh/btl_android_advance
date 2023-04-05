from pydantic import BaseModel

# Article inside UserDisplay
class UserBase(BaseModel):
  username: str
  email: str
  password: str
  class Config():
    orm_mode = True