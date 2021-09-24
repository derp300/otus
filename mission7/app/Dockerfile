FROM python:3.8-slim-buster

COPY ./src /app
WORKDIR /app

RUN pip install --upgrade pip -r requirements.txt

ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH /

EXPOSE 8000

ENTRYPOINT ["python", "main.py"]

