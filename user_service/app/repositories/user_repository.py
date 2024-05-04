from typing import List
from uuid import UUID
from app.models.user import User

# Предопределенные данные о пользователях
users_data = [
    User(id=UUID('85db966c-67f1-411e-95c0-f02edfa5464a'), username='user1', email='user1@example.com'),
    User(id=UUID('31babbb3-5541-4a2a-8201-537cdff25fed'), username='user2', email='user2@example.com'),
    User(id=UUID('45309954-8e3c-4635-8066-b342f634252c'), username='user3', email='user3@example.com'),
    User(id=UUID('88a4f768-3196-41a6-bc97-8b5dfb4f5d76'), username='user4', email='user4@example.com'),
    User(id=UUID('1dc2a3f3-d0bc-4c78-8a2d-04d1e2434f4c'), username='user5', email='user5@example.com')
]

class UserRepo():
    def __init__(self, clear: bool = False) -> None:
        if clear:
            users_data.clear()

    def get_users(self) -> List[User]:
        """Возвращает список всех пользователей."""
        return users_data

    def get_user_by_id(self, user_id: UUID) -> User:
        """Возвращает пользователя по его идентификатору."""
        for user in users_data:
            if user.id == user_id:
                return user
        raise KeyError("User not found")

    def create_user(self, user_data: dict) -> User:
        """
        Создает нового пользователя и добавляет его в список пользователей.
        """
        user = User(**user_data)
        users_data.append(user)
        return user

    def delete_user_by_id(self, user_id: UUID) -> None:
        """
        Удаляет пользователя по его идентификатору.
        """
        for index, user in enumerate(users_data):
            if user.id == user_id:
                del users_data[index]
                return
        raise KeyError("User not found")
