FROM python:3.7-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

RUN pip install pipenv
COPY Pipfile Pipfile.lock /code/
RUN pipenv install --system

COPY . /code/

CMD ["gunicorn", "config.wsgi", "-b 0.0.0.0:8000"]