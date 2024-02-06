"""
Домашнее задание №4
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""

import asyncio
from typing import List, Dict

from jsonplaceholder_requests import fetch_users_data
from jsonplaceholder_requests import fetch_posts_data
from models import Post, Base, async_engine
from models import User
from models import Session


async def create_users_posts_data() -> Dict:
    users_data, posts_data = await asyncio.gather(
        fetch_users_data(),
        fetch_posts_data(),
    )
    return users_data, posts_data


async def create_users_table(
        session: Session,
        users_data: List[dict],
):
    users = [
        User(name=user_data["name"],
             username=user_data["username"],
             email=user_data["email"],
        )
        for user_data in users_data
    ]
    session.add_all(users)
    await session.commit()
    return users

async def create_posts_table(
        session: Session,
        posts_data: List[dict],
):
    posts = [
        Post(
            user_id=post_data["userId"],
            title=post_data["title"],
            body=post_data["body"],
        )
        for post_data in posts_data
    ]
    session.add_all(posts)
    await session.commit()
    return posts


async def async_main():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    async with Session() as session:
        users_data, posts_data = await create_users_posts_data()
        await create_users_table(session, users_data)
        await create_posts_table(session, posts_data)

def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
