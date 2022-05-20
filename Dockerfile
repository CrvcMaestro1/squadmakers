# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt

COPY ./migrate.sh .
RUN sed -i 's/\r$//g' /code/migrate.sh
RUN chmod +x /code/migrate.sh

COPY . /code/

ENTRYPOINT ["/code/migrate.sh"]