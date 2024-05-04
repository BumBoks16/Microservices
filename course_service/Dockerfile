FROM python:3.10

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt


COPY . .
RUN chmod +x /code/startup.sh

CMD ["/code/startup.sh"]