FROM python:3.10

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app
COPY ./migration /code/migration
COPY ./alembic.ini /code/alembic.ini
COPY ./startup.sh /code/startup.sh
RUN chmod +x /code/startup.sh

CMD ["/code/startup.sh"]