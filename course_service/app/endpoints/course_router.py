from fastapi import HTTPException, Path, Body, APIRouter, FastAPI
from typing import List
from uuid import UUID

from app.models.course import Course
from app.services.course_service import CourseService

course_router = APIRouter(prefix="/courses", tags=["Courses"])
app = FastAPI()
# Создаем экземпляр сервиса курсов
course_service = CourseService()


@course_router.get("/courses/", response_model=List[Course])
def get_courses():
    """Получает список всех курсов."""
    return course_service.get_courses()


@course_router.get("/courses/{course_id}", response_model=Course)
def get_course_by_id(course_id: UUID = Path(..., title="The UUID of the course to get")):
    """Получает курс по его идентификатору."""
    return course_service.get_course_by_id(course_id)


@course_router.post("/courses/", response_model=Course)
def create_course(course_data: Course = Body(..., title="The course data to create")):
    """Создает новый курс."""
    return course_service.create_course(course_data)


@course_router.delete("/courses/{course_id}")
def delete_course(course_id: UUID = Path(..., title="The UUID of the course to delete")):
    course_service.delete_course_by_id(course_id)
    return {"message": "Course deleted successfully."}


@course_router.post("/courses/{course_id}/enroll/{user_id}")
def enroll_user(course_id: UUID = Path(..., title="The UUID of the course to enroll"),
                 user_id: UUID = Path(..., title="The UUID of the user to enroll")):
    """Записывает пользователя на курс."""
    course_service.enroll_user(course_id, user_id)
    return {"message": "User enrolled successfully."}
