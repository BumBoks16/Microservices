from app.models.course import Course
from uuid import UUID, uuid4
from pydantic import ValidationError
import pytest

def test_empty_enrolled_users():
    course_data = {
        'id': uuid4(),
        'title': 'Python Programming',
        'description': 'Learn Python programming language from scratch.',
        'enrolled_users': []
    }
    course = Course(
        id=course_data['id'],
        title=course_data['title'],
        description=course_data['description'],
        enrolled_users=course_data['enrolled_users']
    )
    assert course.id == course_data['id']
    assert course.title == course_data['title']
    assert course.description == course_data['description']
    assert course.enrolled_users == course_data['enrolled_users']

def test_id_required():
    course_data = {
        'title': 'Python Programming',
        'description': 'Learn Python programming language from scratch.',
        'enrolled_users': []
    }
    with pytest.raises(ValidationError):
        course = Course(
            title=course_data['title'],
            description=course_data['description'],
            enrolled_users = course_data['enrolled_users']
        )

def test_title_required():
    course_data = {
        'id': uuid4(),
        'description': 'Learn Python programming language from scratch.',
        'enrolled_users': []
    }
    with pytest.raises(ValidationError):
        course = Course(
            id=course_data['id'],
            description=course_data['description'],
            enrolled_users=course_data['enrolled_users']
        )

def test_description_required():
    course_data = {
        'id': uuid4(),
        'title': 'Python Programming',
        'enrolled_users': []
    }
    with pytest.raises(ValidationError):
        course = Course(
            id=course_data['id'],
            title=course_data['title'],
            enrolled_users=course_data['enrolled_users']
        )

def test_non_empty_enrolled_users():
    enrolled_user_data = [
        uuid4(),
        uuid4()
    ]
    course_data = {
        'id': uuid4(),  # Преобразуем UUID в объект типа UUID
        'title': 'Python Programming',
        'description': 'Learn Python programming language from scratch.',
        'enrolled_users': enrolled_user_data
    }
    course = Course(
        id=course_data['id'],
        title=course_data['title'],
        description=course_data['description'],
        enrolled_users=course_data['enrolled_users']
    )
    assert course.id == course_data['id']
    assert course.title == course_data['title']
    assert course.description == course_data['description']
    assert course.enrolled_users == enrolled_user_data