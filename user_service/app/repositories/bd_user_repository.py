from typing import List, Optional
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user import User
from app.schemas.user_schema import User as DBUser

from sqlalchemy.orm import Session
import traceback
from pydantic import BaseModel


# noinspection PyDeprecation
class BdRepo():
    db: Session
    def __init__(self) -> None:
        self.db = next(get_db())

    def _map_to_model(self, user: DBUser) -> User:
        result = User.from_orm(user)
        return result

    def _map_to_schema(self, user: User) -> DBUser:
        data = dict(user)
        result = DBUser(**data)
        return result

    def get_users(self) -> List[User]:
        users = []
        for user in self.db.query(DBUser).all():
            users.append(self._map_to_model(user))
        return users

    def get_user_by_id(self, user_id: int) -> Optional[User]:
        user = self.db.query(DBUser).filter(DBUser.id == user_id).first()
        if user is None:
            return None
        return self._map_to_model(user)

    def create_user(self, user_data: dict) -> User:
        db_user = self._map_to_schema(User(**user_data))
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return self._map_to_model(db_user)

    def delete_user_by_id(self, user_id: int) -> Optional[User]:
        try:
            user = self.db.query(DBUser).filter(DBUser.id == user_id).first()
            if user:
                self.db.delete(user)
                self.db.commit()
                return User.from_orm(user)
            else:
                raise KeyError("User not found")
        except Exception as e:
            traceback.print_exc()
            self.db.rollback()
        return None
