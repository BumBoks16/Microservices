import traceback
from app.services.user_service import UserService
from asyncio import AbstractEventLoop
from uuid import UUID
from aio_pika.abc import AbstractRobustConnection
from aio_pika import connect_robust, IncomingMessage
from app.settings import settings


async def process_create_user(msg: IncomingMessage, user_service: UserService):
    try:
        user_data = msg.body.decode()
        print(user_data)
        # Здесь можно вызвать метод сервиса для создания пользователя
        # Например:
        # await user_service.create_user(user_data)
        await msg.ack()
    except:
        traceback.print_exc()


async def consume(loop: AbstractEventLoop, user_service: UserService) -> AbstractRobustConnection:
    connection = await connect_robust(settings.amqp_url, loop=loop)
    channel = await connection.channel()

    user_created_queue = await channel.declare_queue("user_queue", durable=True)

    await user_created_queue.consume(lambda msg: process_create_user(msg, user_service))
    print('Started RabbitMQ consuming...')

    return connection
