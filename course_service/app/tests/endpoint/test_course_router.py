import pytest
import requests
from uuid import UUID, uuid4
from app.models.course import Course

test_url = "http://127.0.0.1:81/api/courses/courses"

@pytest.fixture(scope='session')
def first_data() -> tuple[dict, dict]:
    data = {
            'id': "d853f0bf-87cd-4c7a-83b1-1698c9fe722b",
            'title': 'Test Course 1',
            'description': 'Test Description 1',
            'enrolled_users': []
            }
    header = {'token': ''}
    return (data, header)

@pytest.fixture(scope='session')
def second_data() -> tuple[dict, dict]:
    data = {
        'id': "03fac1a4-5eae-4397-b411-62c056685b6f",
        'title': 'Test Course 2',
        'description': 'Test Description 2',
        'enrolled_users': []
    }
    header = {'token': ''}
    return (data, header)

def test_get_courses():
    response = requests.get(test_url)
    assert response.status_code == 200

def test_create_course(first_data: tuple[dict, dict]):
    data, header = first_data
    response = requests.post(test_url, json=data, headers=header)
    assert response.status_code == 200
    course = Course.model_validate(response.json())
    assert course.id == UUID(data['id'])
    assert course.title == data['title']
    assert course.description == data['description']
    assert course.enrolled_users == data['enrolled_users']

def test_get_created_course(first_data: tuple[dict, dict]):
    data, header = first_data
    response = requests.get(f"{test_url}/{first_data[0]['id']}", headers=header)
    assert response.status_code == 200

def test_delete_created_course(first_data: tuple[dict, dict]):
    data, header = first_data
    response = requests.delete(f"{test_url}/{first_data[0]['id']}", headers=header)
    assert response.status_code == 200
    response = requests.get(f"{test_url}/{first_data[0]['id']}")
    assert response.status_code == 404

def test_enroll_user(second_data: tuple[dict, dict]):
    data, header = second_data
    response = requests.post(test_url, json=data, headers=header)
    assert response.status_code == 200
    user_id = "3fa85f64-5717-4562-b3fc-2c963f66afa6"
    response = requests.post(f"{test_url}/{second_data[0]['id']}/enroll/{user_id}", headers=header)
    assert response.status_code == 200
    response = requests.delete(f"{test_url}/{second_data[0]['id']}", headers=header)
    assert response.status_code == 200