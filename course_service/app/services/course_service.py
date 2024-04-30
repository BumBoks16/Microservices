from typing import List, Union, Dict
from uuid import UUID

import httpx
from fastapi import HTTPException, requests

from app.models.course import Course
from app.repositories.course_repository import CourseRepo
from fastapi import FastAPI

course_repo = CourseRepo()
app = FastAPI()


class CourseService:
    def __init__(self):
        self.course_repo = course_repo

    def get_courses(self) -> List[Course]:
        """Получает список всех курсов."""
        return self.course_repo.get_courses()

    def get_course_by_id(self, course_id: UUID) -> Course:
        """Получает курс по его идентификатору."""
        try:
            return self.course_repo.get_course_by_id(course_id)
        except KeyError:
            raise HTTPException(status_code=404, detail="Course not found")

    def create_course(self, course_data: dict) -> Course:
        """Создает новый курс и возвращает его идентификатор."""
        return self.course_repo.create_course(course_data.dict())

    def delete_course_by_id(self, course_id: UUID) -> None:
        """Удаляет курс по его идентификатору."""
        try:
            self.course_repo.delete_course_by_id(course_id)
        except KeyError:
            raise HTTPException(status_code=404, detail="Course not found")

    def enroll_user(self, course_id: UUID, user_id: UUID) -> None:
        """Записывает пользователя на курс."""
        # Здесь вы можете отправить HTTP-запрос к другому сервису для получения информации о пользователе
        response = httpx.get(f"http://user-service:80/api/users/{user_id}")
        print(response.content)
        if response.status_code == 200:
            user_data = response.json()
            # После получения данных о пользователе, вы можете вызвать метод вашего репозитория для записи пользователя на курс
            self.course_repo.enroll_user(course_id, user_data)
        else:
            # Обработка случаев, когда не удалось получить данные о пользователе
            raise Exception("Failed to fetch user data from other service")
