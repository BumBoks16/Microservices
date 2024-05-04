from fastapi import FastAPI, HTTPException, APIRouter
from app.settings import settings
from typing import List
from uuid import UUID
from app.models.user import User
from app.repositories.bd_user_repository import BdRepo
from app.repositories.user_repository import UserRepo

app = FastAPI()

# Создаем экземпляр репозитория пользователей
if not settings.is_local:
    user_repo = BdRepo()
else:
    user_repo = UserRepo

# Создаем APIRouter для пользователей
user_router = APIRouter(prefix="/users", tags=["Users"])

@user_router.get("/", response_model=List[User])
def get_users():
    """
    Получает список всех пользователей.
    """
    return user_repo.get_users()

@user_router.get("/{user_id}", response_model=User)
def get_user(user_id: UUID):
    """
    Получает пользователя по его идентификатору.
    """
    try:
        return user_repo.get_user_by_id(user_id)
    except KeyError:
        raise HTTPException(status_code=404, detail="User not found")

@user_router.post("/", response_model=User)
def create_user(user_data: dict):
    """
    Создает нового пользователя.
    """
    return user_repo.create_user(user_data)

@user_router.delete("/{user_id}", response_model=None)
def delete_user(user_id: UUID):
    """
    Удаляет пользователя по его идентификатору.
    """
    try:
        user_repo.delete_user_by_id(user_id)
        return None
    except KeyError:
        raise HTTPException(status_code=404, detail="User not found")

# Включаем роутер пользователей в приложение
app.include_router(user_router)


"""def validate_user(token: str):
    if settings.test_build:
        return
    userdata = check_token(token)
    if userdata.status_code != 200:
        raise ValueError"""