from datetime import date
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


# signin
class UserLogin(BaseModel):
    user_id: str
    user_pw: str


class Token(BaseModel):
    Authorization: str


class UserToken(BaseModel):
    uid: int
    user_id: str
    # user_pw: str
    user_name: str
    phone_number: str
    # create_date: date

    class Config:
        orm_mode = True


class PostCreate(BaseModel):
    title: str
    content: str
    create_date: date

    class Config:
        orm_mode = True


class CommentCreate(BaseModel):
    content: str
    create_date: date
