from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base
from app.models.user import User


Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(UUID(as_uuid=True), primary_key=True)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)

    class Config:
        orm_mode = True
        from_attributes = True
