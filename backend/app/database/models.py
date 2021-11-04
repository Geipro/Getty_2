from sqlalchemy import Boolean, Column, ForeignKey, String, Integer, Date
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import null
from sqlalchemy.sql.sqltypes import DateTime

from .database import Base


class Client(Base):
    __tablename__ = "client"

    cid = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
        nullable=False,
        comment="고객 고유 ID",
    )
    user_name = Column(String(45), nullable=True, comment="고객 이름")
    user_id = Column(String(45), nullable=True, comment="고객 ID")
    user_pw = Column(String(300), nullable=True, comment="고객 PW")
    create_date = Column(Date, nullable=True, comment="생성 날짜")
    phone_number = Column(String(45), nullable=True, comment="전화 번호")

    address = Column(String(45), nullable=True, comment="주소")
    job = Column(String(45), nullable=False, comment="직업")
    birth = Column(String(45), nullable=False, comment="생년월일")
    sex = Column(Integer, nullable=False, comment="성별")
