from typing import List
from uuid import UUID
from app.models.course import Course

# Предопределенные данные о курсах
courses_data = [
    Course(id=UUID('a7f7b747-3d5d-4c90-b365-fd88e39d8ec4'), title='Course 1', description='Description 1', enrolled_users=[]),
    Course(id=UUID('be83652c-85ad-4d2b-8c86-5e36e76f62f3'), title='Course 2', description='Description 2', enrolled_users=[]),
    Course(id=UUID('1d70c9f2-6782-40ac-8d79-b1b8e48f9a24'), title='Course 3', description='Description 3', enrolled_users=[]),
    Course(id=UUID('fa08a78a-69a7-46b6-97a4-81d497ea73e2'), title='Course 4', description='Description 4', enrolled_users=[]),
    Course(id=UUID('57b7fd94-8b5e-4041-9cd5-5b17c84e3497'), title='Course 5', description='Description 5', enrolled_users=[])
]

class CourseRepo:
    def __init__(self, clear: bool = False) -> None:
        if clear:
            courses_data.clear()

    def get_courses(self) -> List[Course]:
        """Возвращает список всех курсов."""
        return courses_data

    def get_course_by_id(self, course_id: UUID) -> Course:
        """Возвращает курс по его идентификатору."""
        for course in courses_data:
            if course.id == course_id:
                return course
        raise KeyError("Course not found")

    def create_course(self, course_data: dict) -> Course:
        """
        Создает новый курс и добавляет его в список курсов.
        """
        course_id = course_data.get('id')
        if course_id in [course.id for course in courses_data]:
            raise KeyError(f"Course with id {course_id} already exists.")
        course = Course(**course_data)
        courses_data.append(course)
        return course

    def delete_course_by_id(self, course_id: UUID) -> None:
        """
        Удаляет курс по его идентификатору.
        """
        for index, course in enumerate(courses_data):
            if course.id == course_id:
                del courses_data[index]
                return
        raise KeyError("Course not found")

    def enroll_user(self, course_id: UUID, user_id: UUID) -> None:
        """
        Записывает пользователя на курс.
        """
        course = self.get_course_by_id(course_id)
        course.enrolled_users.append(user_id)

    def get_enrolled_users(self, course_id: UUID) -> List[UUID]:
        """
        Возвращает список идентификаторов пользователей, записанных на курс.
        """
        course = self.get_course_by_id(course_id)
        return course.enrolled_users