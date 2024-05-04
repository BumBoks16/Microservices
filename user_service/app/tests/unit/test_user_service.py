from app.models.user import User
from app.services.user_service import UserService
from uuid import UUID, uuid4
from pydantic import ValidationError
from fastapi import HTTPException
import pytest
from app import settings


@pytest.fixture(scope='session')
def user_service() -> UserService:
    return UserService()


@pytest.fixture(scope='session')
def first_data() -> UUID:
    return uuid4()


@pytest.fixture(scope='session')
def second_data() -> UUID:
    return uuid4()


def test_get_repo_users(user_service: UserService):
    settings.is_local = True
    assert user_service.get_users() == [
        User(id=UUID('85db966c-67f1-411e-95c0-f02edfa5464a'), username='user1', email='user1@example.com'),
        User(id=UUID('31babbb3-5541-4a2a-8201-537cdff25fed'), username='user2', email='user2@example.com'),
        User(id=UUID('45309954-8e3c-4635-8066-b342f634252c'), username='user3', email='user3@example.com'),
        User(id=UUID('88a4f768-3196-41a6-bc97-8b5dfb4f5d76'), username='user4', email='user4@example.com'),
        User(id=UUID('1dc2a3f3-d0bc-4c78-8a2d-04d1e2434f4c'), username='user5', email='user5@example.com')]
    settings.is_local = False


def test_get_non_existing_user(second_data: UUID, user_service: UserService):
    with pytest.raises(HTTPException) as exc_info:
        user_service.get_user_by_id(second_data)
    assert exc_info.value.status_code == 404


def test_create_user(first_data: UUID, user_service: UserService):
    user_id = first_data
    username = 'test_user'
    email = 'test@example.com'
    user_data = {'id': user_id, 'username': username, 'email': email}
    created_user_id = user_service.create_user(user_data)
    assert created_user_id == user_id

def test_delete_non_existing_user(second_data: UUID, user_service: UserService):
    with pytest.raises(HTTPException) as exc_info:
        user_service.delete_user_by_id(second_data)
    assert exc_info.value.status_code == 404


def test_get_existing_user(first_data: UUID, user_service: UserService):
    user_id = first_data
    user_data = {
        "id": user_id,
        "username": "test_user",
        "email": "test@example.com"
    }
    user_service.create_user(user_data)
    expected_user = User(**user_data)
    assert user_service.get_user_by_id(user_id) == expected_user
