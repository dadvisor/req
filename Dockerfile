FROM python:3.6-slim

WORKDIR /app
COPY . /app

RUN pip install requests


CMD ["python", "-u", "main.py"]
