from datetime import datetime, timedelta
from typing import Optional
from fastapi import FastAPI, APIRouter, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware

import bcrypt, jwt
import os

from sqlalchemy.orm import Session
from database import schemas, models, crud
from database.database import SessionLocal, engine
from common.consts import (
    JWT_SECRET,
    JWT_ALGORITHM,
)

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Cors
origins = []
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def create_access_token(*, data: dict = None, expires_delta: int = None):
    to_encode = data.copy()
    if expires_delta:
        to_encode.update({"exp": datetime.utcnow() + timedelta(hours=expires_delta)})
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET, algorithm=JWT_ALGORITHM)

    return encoded_jwt


@app.post("/signup", status_code=200, response_model=schemas.User)
async def signup(user_info: schemas.UserCreate, db: Session = Depends(get_db)):
    """
    `회원가입 API`\n
    :param user:s
    :param db:
    :return:
    """
    db_user = crud.get_user_by_userid(db, user_id=user_info.user_id)
    if db_user:
        raise HTTPException(status_code=400, detail="user_id already registered")

    return crud.create_user(db=db, user=user_info)


@app.post("/signin", status_code=200, response_model=schemas.Token)
async def signin(user_info: schemas.UserLogin, db: Session = Depends(get_db)):
    """
    `로그인 API`\n
    :param user_info:
    :param db:
    :return:
    """
    if not user_info.user_id or not user_info.user_pw:
        raise HTTPException(
            status_code=400, detail="user_id and user_pw must be provided"
        )

    get_user = crud.get_user_by_userid(db, user_id=user_info.user_id)
    if not get_user:
        raise HTTPException(status_code=400, detail="no match user")

    pw_verified = bcrypt.checkpw(
        user_info.user_pw.encode("utf-8"), get_user.user_pw.encode("utf-8")
    )

    if not pw_verified:
        raise HTTPException(status_code=400, detail="No match user : Wrong password")

    token = dict(
        Authorization=f"{create_access_token(data=schemas.UserToken.from_orm(get_user).dict(exclude={'user_pw', 'create_date'}),)}"
    )

    return token
