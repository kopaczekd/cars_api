FROM python:3.8-slim-buster

EXPOSE 8000

ENV PYTHONUNBUFFERED=1 \
    PORT=8000

WORKDIR /app

ADD . .

RUN pip install --upgrade pip
RUN pip install pipenv
RUN pipenv install --skip-lock --system --dev
