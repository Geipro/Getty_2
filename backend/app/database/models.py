from sqlalchemy import Boolean, Column, ForeignKey, String, Integer, Date, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import null
from sqlalchemy.sql.sqltypes import DateTime

from .database import Base


class User(Base):
    __tablename__ = "user"

    uid = Column(
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

    # address = Column(String(45), nullable=True, comment="주소")
    # job = Column(String(45), nullable=False, comment="직업")
    birth = Column(String(45), nullable=False, comment="생년월일")
    sex = Column(Integer, nullable=False, comment="성별")


class Post(Base):
    __tablename__ = "post"

    pid = Column(
        Integer, primary_key=True, autoincrement=True, nullable=False, comment="게시글 ID"
    )
    uid = Column(
        Integer,
        ForeignKey("user.uid", ondelete="RESTRICT", onupdate="RESTRICT"),
        nullable=False,
        comment="고객 ID",
    )

    title = Column(String(100), nullable=False, comment="제목")
    content = Column(Text, nullable=False, comment="내용")
    hit = Column(Integer, nullable=False, comment="조회수", default=0)

    create_date = Column(Date, nullable=False, comment="작성일")

    # is_parent = Column(Boolean, nullable=False, comment="게시글/댓글 구별")


class Comment(Base):
    __tablename__ = "comment"

    cid = Column(
        Integer, primary_key=True, autoincrement=True, nullable=False, comment="댓글 ID"
    )
    uid = Column(
        Integer,
        ForeignKey("user.uid", ondelete="RESTRICT", onupdate="RESTRICT"),
        nullable=False,
        comment="고객 ID",
    )
    pid = Column(
        Integer,
        ForeignKey("post.pid", ondelete="RESTRICT", onupdate="RESTRICT"),
        nullable=False,
        comment="게시글 ID",
    )

    content = Column(Text, nullable=False, comment="내용")
    create_date = Column(Date, nullable=False, comment="작성일")
