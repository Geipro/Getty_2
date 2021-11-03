import abc
from datetime import date
from typing import List, Optional
from pydantic import BaseModel


class User(BaseModel):
    user_id: str
    user_name: str

    phone_number: str
    create_date: date
    address: str
    job: str
    birth: str
    sex: int

    class Config:
        orm_mode = True


# signup
class UserCreate(BaseModel):
    user_id: str
    user_pw: str
    user_name: str

    phone_number: str
    job: str
    birth: str
    sex: int
