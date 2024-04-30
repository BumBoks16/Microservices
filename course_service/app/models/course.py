from typing import List
from uuid import UUID
from pydantic import BaseModel, Field


class Course(BaseModel):
    id: UUID
    title: str
    description: str
    enrolled_users: List[UUID] = []