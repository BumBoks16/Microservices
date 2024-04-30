from fastapi import FastAPI
from app.models import course
from app.services.course_service import CourseService
from app.endpoints.course_router import course_router

app = FastAPI(title='Course Service')

app.include_router(course_router, prefix='/api')
