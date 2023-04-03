from typing import Optional
from pydantic import BaseModel


class LoginForm(BaseModel):
    email: str
    password: str


class SignUpForm(BaseModel):
    full_name: Optional[str]
    phone_number: Optional[str]
    email: str
    password: str
    personal_number: Optional[str]
    address: Optional[str]
    activate: Optional[bool] = False
    birth_day: Optional[str]
