from fastapi import FastAPI, HTTPException
from typing import List
from uuid import UUID
from fastapi.exceptions import HTTPException


from app.database import get_db
from app.models.user import User
from app.repositories.bd_user_repository import BdRepo
from app.repositories.user_repository import UserRepo
from app.settings import settings

app = FastAPI()

# Создаем экземпляр репозитория пользователей
user_repo = UserRepo()
bd_user_repo = BdRepo()


# noinspection PyTypeChecker
class UserService():
    def __init__(self) -> None:
        if settings.is_local:
            self.user_repo = user_repo
        else:
            self.user_repo = bd_user_repo

    def get_users(self) -> List[User]:
        """
        Получает список всех пользователей.
        """
        return self.user_repo.get_users()

    def get_user_by_id(self, user_id: UUID) -> User:
        """
        Получает пользователя по его идентификатору.
        """
        try:
            return self.user_repo.get_user_by_id(user_id)
        except KeyError:
            raise HTTPException(status_code=404, detail="User not found")

    def create_user(self, user_data: dict) -> int:
        """
        Создает нового пользователя и возвращает его идентификатор.
        """
        user = self.user_repo.create_user(user_data)
        return user.id

    def delete_user_by_id(self, user_id: UUID) -> None:
        """
        Удаляет пользователя по его идентификатору.
        """
        try:
            self.user_repo.delete_user_by_id(user_id)
        except KeyError:
            raise HTTPException(status_code=404, detail="User not found")