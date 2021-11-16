from datetime import datetime, timedelta
from typing import Optional
from fastapi import FastAPI, APIRouter, Depends, HTTPException, Header
from fastapi.middleware.cors import CORSMiddleware

import bcrypt, jwt
import os
from dotenv import load_dotenv

from bs4 import BeautifulSoup
import requests
import re


# getUpbit.py
from chart.getUpbit import coin_list, get_coin_symbol, update_coin_data, sort_by

# getFinanceData.py
import finance.getFinanceData as getFD

from sqlalchemy.orm import Session
from database import schemas, models, crud
from database.database import SessionLocal, engine
from common.consts import (
    JWT_SECRET,
    JWT_ALGORITHM,
)

models.Base.metadata.create_all(bind=engine)

load_dotenv()

if os.environ.get("LOCAL") != "True":
    app = FastAPI(root_path="/backend")  # Server
else:
    app = FastAPI()  # Local

# Cors
origins = [
    "https://localhost.tiangolo.com",
    "http://localhost.tiangolo.com",
    "https://localhost:8080",
    "https://localhost:8000",
    "http://localhost:8080",
    "http://localhost:8000",
    "https://k5a405.p.ssafy.io:8000",
    "https://k5a405.p.ssafy.io",
    "http://localhost",
    "http://k5a405.p.ssafy.io:8000",
]
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

    return crud.create_post(db=db, post=post_info, uid=user.uid, user_id=user_id)


@app.get("/posts", status_code=200)
async def get_all_post(db: Session = Depends(get_db)):
    """
    `모든 게시글 가져오기`
    :param db:
    :return:
    """
    return crud.get_all_post(db=db)


@app.get("/my_post", status_code=200)
async def get_my_post(
    token: str = Header(None),
    db: Session = Depends(get_db),
):
    """
    `내 게시글 가져오기`
    :header token:
    :param db:
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


@app.get("/post", status_code=200)
async def get_post(pid: int, db: Session = Depends(get_db)):
    """
    `특정 게시물(1개) 가져오기`
    :param pid:
    :param db:
    :return:
    """

    return crud.get_post_by_pid(db=db, pid=pid)


@app.get("/post", status_code=200)
async def get_post(pid: int, db: Session = Depends(get_db)):
    """
    `특정 게시물 가져오기`
    :param pid:
    :param db:
    :return:
    """

    return crud.get_post_by_pid(db=db, pid=pid)


@app.get("/my_comment", status_code=200)
async def get_my_comment(token: str = Header(None), db: Session = Depends(get_db)):
    """
    `내 댓글 가져오기`
    :header token:
    :param db:
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

    return crud.get_user_comment_by_uid(db=db, uid=user.uid)


@app.get("/comment", status_code=200)
async def get_comment(pid: int, db: Session = Depends(get_db)):
    """
    `특정 게시물의 댓글 가져오기`
    :param post_id:
    :param db:
    :return:
    """

    return crud.get_comment_by_pid(db=db, pid=pid)


@app.post("/comment", status_code=200)
async def create_comment(
    comment_info: schemas.CommentCreate,
    pid: int,
    token: str = Header(None),
    db: Session = Depends(get_db),
):
    """
    `댓글 생성`
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

    return crud.create_comment(
        db=db, comment=comment_info, uid=user.uid, pid=pid, user_id=user_id
    )


@app.get("/sort", status_code=200)
async def sorting_chart(reverse_flag: bool, case: str, db: Session = Depends(get_db)):
    """
    `차트 정렬`
    :param db:
    :param reverse_flag:
    :return:
    """
    get_coin_symbol()
    new_data = update_coin_data()
    # print(new_data)

    return sorted(new_data, key=lambda x: x[case], reverse=reverse_flag)


@app.get("/deposit", status_code=200)
async def get_deposit(db: Session = Depends(get_db)):
    """
    `정기 예금 데이터 가져오기`
    :param db:
    :return:
    """
    getFD.getDeposit()

    return getFD.deposit_list


@app.get("/saving", status_code=200)
async def get_saving(db: Session = Depends(get_db)):
    """
    `적금 데이터 가져오기`
    :param db:
    :return:
    """
    getFD.getSaving()

    return getFD.saving_list


@app.get("/mortgage", status_code=200)
async def get_mortgage(db: Session = Depends(get_db)):
    """
    `주택담보대출 API 가져오기`
    :param db:
    :return:
    """
    getFD.getMortgage()

    return getFD.mortgage_list


@app.get("/renthouse", status_code=200)
async def get_renthouse(db: Session = Depends(get_db)):
    """
    `전세자금 API 가져오기`
    :param db:
    :return:
    """
    getFD.getRentHouse()

    return getFD.rentHouse_list


@app.get("/credit_loan", status_code=200)
async def get_credit_loan(db: Session = Depends(get_db)):
    """
    `개인신용대출 API 가져오기`
    :param db:
    :return:
    """
    getFD.getcreditLoan()

    return getFD.creditLoan_list


@app.get("/news/{query}")
def read_item(query: str):
    query = query.replace(' ', '+') 
    news_num = 18
    news_url = 'https://search.naver.com/search.naver?where=news&sm=tab_jum&query={}'
    req = requests.get(news_url.format(query))
    soup = BeautifulSoup(req.text, 'html.parser')

    news_dict = {} 
    cur_page = 1
    idx = 0

    while idx < news_num:
        table = soup.find('ul',{'class' : 'list_news'})
        li_list = table.find_all('li', {'id': re.compile('sp_nws.*')})
        area_list = [li.find('div', {'class' : 'news_area'}) for li in li_list]
        a_list = [area.find('a', {'class' : 'news_tit'}) for area in area_list]
        desc_list = [li.find('div', {'class':'news_dsc'}).find('div', {'class':'dsc_wrap'}).get_text() for li in li_list]

        thumbnail_list = []
        for li in li_list:
            try:
                thumbnail_list.append(li.find('a', {'class': 'dsc_thumb'}).find('img').get('src'))
            except:
                thumbnail_list.append('')

        for i in range(len(a_list[:min(len(a_list), news_num-idx)])):
            n = a_list[i]
            title = n.get('title')
            url = n.get('href')
            thumbnail = thumbnail_list[i]
            desc = desc_list[i]
            news_dict[idx] = {
                'title': title,
                'url': url,
                'thumbnail': thumbnail,
                'desc': desc,
            }
            idx += 1
        cur_page += 1
        
        pages = soup.find('div', {'class' : 'sc_page_inner'})
        print(pages)
        next_page_url = [p for p in pages.find_all('a') if p.text == str(cur_page)][0].get('href')
        
        req = requests.get('https://search.naver.com/search.naver' + next_page_url)
        soup = BeautifulSoup(req.text, 'html.parser')

    return news_dict