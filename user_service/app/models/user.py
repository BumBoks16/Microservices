from uuid import UUID
from pydantic import BaseModel, Field


class User(BaseModel):
    id: UUID
    username: str
    email: str

    class Config:
        orm_mode = True
        from_attributes = True
