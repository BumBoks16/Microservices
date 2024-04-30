from app.models.user import User
from uuid import UUID, uuid4
from pydantic import ValidationError
import pytest

def test_create():
    user_data = {
        'id': uuid4(),
        'username': 'Антон Кришковец',
        'email': 'anton@gmail.com'
    }
    user = User(
        id=user_data['id'],
        username=user_data['username'],
        email=user_data['description']
    )
    assert user.id == user_data['id']
    assert user.username == user_data['username']
    assert user.email == user_data['email']

def test_id_required():
    user_data = {
        'username': 'Антон Кришковец',
        'email': 'anton@gmail.com'
    }
    with pytest.raises(ValidationError):
        user = User(
            username=user_data['username'],
            email=user_data['email']
        )

def test_name_required():
    user_data = {
        'id': uuid4(),
        'email': 'anton@gmail.com'
    }
    with pytest.raises(ValidationError):
        user = User(
            id=user_data['id'],
            email=user_data['email']
        )

def test_email_required():
    user_data = {
        'id': uuid4(),
        'username': 'Антон Кришковец'
    }
    with pytest.raises(ValidationError):
        user= User(
            id=user_data['id'],
            name=user_data['username']
        )