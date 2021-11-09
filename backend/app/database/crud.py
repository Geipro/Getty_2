from . import models, schemas
from sqlalchemy.orm import Session
from datetime import date

import bcrypt


def get_user_by_uid(db: Session, uid: int):
    return db.query(models.User).filter(models.User.uid == uid).first()


def get_user_by_userid(db: Session, user_id: str):
    return db.query(models.User).filter(models.User.user_id == user_id).first()


def get_user_post_by_uid(db: Session, uid: int):
    return db.query(models.Post).filter(models.Post.uid == uid).all()


def get_user_comment_by_uid(db: Session, uid: int):
    return db.query(models.Comment).filter(models.Comment.uid == uid).all()


def get_comment_by_pid(db: Session, pid: int):
    return db.query(models.Comment).filter(models.Comment.pid == pid).all()


def get_all_post(db: Session):
    return db.query(models.Post).all()


def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = bcrypt.hashpw(user.user_pw.encode("utf-8"), bcrypt.gensalt())
    create_now = date.today()
    db_user = models.User(
        user_id=user.user_id,
        user_pw=hashed_password,
        user_name=user.user_name,
        phone_number=user.phone_number,
        create_date=create_now,
        # job=user.job,
        birth=user.birth,
        sex=user.sex,
        # address="",
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


def create_post(db: Session, post: schemas.PostCreate, uid: int, user_id: str):
    create_now = date.today()
    db_post = models.Post(
        title=post.title,
        content=post.content,
        hit=0,
        uid=uid,
        user_id=user_id,
        create_date=str(create_now),
    )

    db.add(db_post)
    db.commit()
    db.refresh(db_post)

    return db_post


def create_comment(
    db: Session, comment: schemas.CommentCreate, uid: int, pid: int, user_id: str
):
    create_now = date.today()
    db_comment = models.Comment(
        content=comment.content,
        create_date=str(create_now),
        uid=uid,
        user_id=user_id,
        pid=pid,
    )

    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)

    return db_comment
