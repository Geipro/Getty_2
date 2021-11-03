from . import models, schemas
from sqlalchemy.orm import Session
from datetime import date

import bcrypt


def get_user_by_userid(db: Session, user_id: str):
    return db.query(models.Client).filter(models.Client.user_id == user_id).first()


def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = bcrypt.hashpw(user.user_pw.encode("utf-8"), bcrypt.gensalt())
    create_now = date.today()
    db_user = models.Client(
        user_id=user.user_id,
        user_pw=hashed_password,
        user_name=user.user_name,
        phone_number=user.phone_number,
        create_date=create_now,
        job=user.job,
        birth=user.birth,
        sex=user.sex,
        address="",
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user
