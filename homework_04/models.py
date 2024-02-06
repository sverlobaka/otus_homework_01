"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""

import os

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship

PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+asyncpg://postgres:password@localhost/postgres"
DB_ECHO = False

async_engine = create_async_engine(
    url=PG_CONN_URI,
    echo=DB_ECHO,
)

class Base(DeclarativeBase):
    id = Column(Integer, primary_key=True)


Session = async_sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

class User(Base):
    __tablename__ = "users"
    name = Column(
        String(32),
        nullable=False,
        unique=False,
    )

    username = Column(
        String(50),
        nullable=False,
        unique=True,

    )

    email = Column(
        String,
        nullable=False,
        unique=True,
    )

    posts = relationship(
        "Post",
        back_populates="user",
        uselist=True,
    )


class Post(Base):
    __tablename__ = "posts"
    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        unique=False,
        nullable=False,
    )

    title = Column(
        String(100),
        nullable=False,
    )

    body = Column(
        String,
        unique=False,
        nullable=True,
    )

    user = relationship(
        "User",
        back_populates="posts",
        uselist=False,
    )
