import pytest
from uuid import UUID, uuid4
from app.repositories.course_repository import CourseRepo, Course

@pytest.fixture(scope='session')
def course_repo() -> CourseRepo:
    return CourseRepo()

@pytest.fixture(scope='session')
def course_id() -> UUID:
    return uuid4()

@pytest.fixture(scope='session')
def user_id() -> UUID:
    return uuid4()

def test_get_courses(course_repo: CourseRepo):
    # Проверяем получение списка курсов
    courses = course_repo.get_courses()
    assert isinstance(courses, list)

def test_get_course_by_id_existing(course_id: UUID, course_repo: CourseRepo):
    # Создаем курс и проверяем его получение по идентификатору
    course_data = {"id": course_id, "title": "Test Course", "description": "Test Description", "enrolled_users": []}
    course_repo.create_course(course_data)
    assert course_repo.get_course_by_id(course_id).id == course_id

def test_get_course_by_id_non_existing(course_id: UUID, course_repo: CourseRepo):
    # Пытаемся получить несуществующий курс и проверяем, что вызывается исключение KeyError
    with pytest.raises(KeyError):
        course_repo.get_course_by_id(course_id)

def test_create_course(course_id: UUID, course_repo: CourseRepo):
    # Создаем курс и проверяем его создание
    course_data = {"id": course_id, "title": "Test Course", "description": "Test Description", "enrolled_users": []}
    course = course_repo.create_course(course_data)
    assert course.id == course_id

def test_create_duplicate_course(course_id: UUID, course_repo: CourseRepo):
    # Создаем курс с уже существующим идентификатором и проверяем, что вызывается исключение KeyError
    course_data = {"id": course_id, "title": "Test Course", "description": "Test Description", "enrolled_users": []}
    course_repo.create_course(course_data)
    with pytest.raises(KeyError):
        course_repo.create_course(course_data)

def test_delete_course_existing(course_id: UUID, course_repo: CourseRepo):
    # Создаем курс и удаляем его, проверяем что его больше нет в списке
    course_data = {"id": course_id, "title": "Test Course", "description": "Test Description", "enrolled_users": []}
    course_repo.create_course(course_data)
    course_repo.delete_course_by_id(course_id)
    with pytest.raises(KeyError):
        course_repo.get_course_by_id(course_id)

def test_delete_course_non_existing(course_id: UUID, course_repo: CourseRepo):
    # Пытаемся удалить несуществующий курс и проверяем, что вызывается исключение KeyError
    with pytest.raises(KeyError):
        course_repo.delete_course_by_id(course_id)

def test_enroll_user(course_id: UUID, user_id: UUID, course_repo: CourseRepo):
    # Создаем курс и пользователя, записываем пользователя на курс и проверяем его наличие в списке записанных
    course_data = {"id": course_id, "title": "Test Course", "description": "Test Description", "enrolled_users": []}
    course_repo.create_course(course_data)
    course_repo.enroll_user(course_id, user_id)
    enrolled_users = course_repo.get_enrolled_users(course_id)
    assert user_id in enrolled_users

def test_enroll_user_non_existing_course(course_id: UUID, user_id: UUID, course_repo: CourseRepo):
    # Пытаемся записать пользователя на несуществующий курс и проверяем, что вызывается исключение KeyError
    with pytest.raises(KeyError):
        course_repo.enroll_user(course_id, user_id)

def test_get_enrolled_users(course_id: UUID, user_id: UUID, course_repo: CourseRepo):
    # Создаем курс, записываем пользователя на курс и проверяем список записанных пользователей
    course_data = {"id": course_id, "title": "Test Course", "description": "Test Description", "enrolled_users": []}
    course_repo.create_course(course_data)
    course_repo.enroll_user(course_id, user_id)
    enrolled_users = course_repo.get_enrolled_users(course_id)
    assert len(enrolled_users) == 1
    assert user_id in enrolled_users

def test_get_enrolled_users_empty(course_id: UUID, course_repo: CourseRepo):
    # Создаем курс и проверяем, что список записанных пользователей пуст
    course_data = {"id": course_id, "title": "Test Course", "description": "Test Description", "enrolled_users": []}
    course_repo.create_course(course_data)
    enrolled_users = course_repo.get_enrolled_users(course_id)
    assert len(enrolled_users) == 0