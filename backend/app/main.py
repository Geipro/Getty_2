from datetime import datetime, timedelta
from typing import Optional
from fastapi import FastAPI, APIRouter, Depends, HTTPException, Header
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

app = FastAPI(root_path="/backend")

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
async def sign_up(user_info: schemas.UserCreate, db: Session = Depends(get_db)):
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
async def sign_in(user_info: schemas.UserLogin, db: Session = Depends(get_db)):
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

    is_exist = crud.get_user_by_userid(db, user_id=user_info.user_id)
    if not is_exist:
        raise HTTPException(status_code=400, detail="no match user")

    is_verified = bcrypt.checkpw(
        user_info.user_pw.encode("utf-8"), is_exist.user_pw.encode("utf-8")
    )

    if not is_verified:
        raise HTTPException(status_code=400, detail="No match user : Wrong password")

    token = dict(
        Authorization=f"{create_access_token(data=schemas.UserToken.from_orm(is_exist).dict(exclude={'user_pw', 'create_date'}))}"
    )

    return token


@app.get("/test/get_user", status_code=200)
async def get_user(db: Session = Depends(get_db), token: str = Header(None)):
    """
    `토큰 decode test`\n
    :header token:
    :return:
    """
    if token == None:
        raise HTTPException(status_code=400, detail="Header doesn't have Auth Token")
    payload = jwt.decode(token, JWT_SECRET, algorithms=JWT_ALGORITHM)
    user_id = payload.get("user_id")
    if user_id is None:
        raise HTTPException(status_code=400, detail="NO_MATCH_USER")
    user = crud.get_user_by_userid(db, user_id=user_id)

    return user


@app.get("/post", status_code=200)
async def get_my_post(
    token: str = Header(None),
    db: Session = Depends(get_db),
):
    """
    `게시글 생성`
    :header token:
    :param db:
    :param post_id:
    :return:
    """
    if token == None:
        raise HTTPException(status_code=400, detail="Header doesn't have Auth Token")
    payload = jwt.decode(token, JWT_SECRET, algorithms=JWT_ALGORITHM)
    user_id = payload.get("user_id")
    if user_id is None:
        raise HTTPException(status_code=400, detail="NO_MATCH_USER")
    # print("test gogo")
    user = crud.get_user_by_userid(db, user_id=user_id)

    return crud.get_user_post_by_uid(db=db, uid=user.uid)


@app.post("/post", status_code=200)
async def create_post(
    post_info: schemas.PostCreate,
    token: str = Header(None),
    db: Session = Depends(get_db),
):
    """
    `게시글 생성`
    :header token:
    :param db:
    :param post_id:
    :return:
    """
    if token == None:
        raise HTTPException(status_code=400, detail="Header doesn't have Auth Token")
    payload = jwt.decode(token, JWT_SECRET, algorithms=JWT_ALGORITHM)
    user_id = payload.get("user_id")
    if user_id is None:
        raise HTTPException(status_code=400, detail="NO_MATCH_USER")
    # print("test gogo")
    user = crud.get_user_by_userid(db, user_id=user_id)

    return crud.create_post(db=db, post=post_info, uid=user.uid)
