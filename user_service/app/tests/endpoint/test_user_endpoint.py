import pytest
import requests
from uuid import uuid4
from app.models.user import User

test_url = "http://127.0.0.1:80/api/users"


# Фикстура для создания пользователя
@pytest.fixture(scope='session')
def user_data() -> dict:
    data = {
        'id': '35775fad-6d3c-431f-8f3e-a778e3a2e437',
        'username': 'test_user',
        'email': 'test@example.com'
    }
    return data


# Тест получения списка пользователей
def test_get_users(user_data: dict):
    response = requests.get(test_url)
    assert response.status_code == 200
    users = response.json()
    # Проверяем, что полученный список не пустой
    assert len(users) > 0


# Тест создания нового пользователя
def test_create_user(user_data: dict):
    response = requests.post(test_url, json=user_data)
    assert response.status_code == 200


# Тест получения данных пользователя по его идентификатору
def test_get_user_by_id(user_data: dict):
    # Получаем данные пользователя по его идентификатору
    response = requests.get(f"{test_url}/{user_data['id']}")
    assert response.status_code == 200


def test_delete_user(user_data: dict):
    # Создаем пользователя
    response = requests.delete(f"{test_url}/{user_data['id']}")
    assert response.status_code == 200

    get_response = requests.get(f"{test_url}/{user_data['id']}")
    assert get_response.status_code == 404


def test_get_nonexistent_user():
    response = requests.get(f"{test_url}/{uuid4()}")
    assert response.status_code == 404
    assert response.json()['detail'] == "User not found"
