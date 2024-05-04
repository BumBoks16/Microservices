from fastapi import FastAPI
from app.endpoints.user_endpoint import user_router
from app.services.user_service import UserService
from app.rabbitmq import rabbit
import time
from app.settings import settings
import asyncio


app = FastAPI(title='User Service')

# Создаем экземпляр сервиса пользователей
user_service = UserService()

# Подключаемся и начинаем потреблять сообщения из RabbitMQ
if not settings.is_local:
    @app.on_event("startup")
    async def startup_event():
        time.sleep(15)
        loop = asyncio.get_event_loop()
        asyncio.ensure_future(rabbit.consume(loop, user_service))


app.include_router(user_router, prefix='/api')