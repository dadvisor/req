FROM python:3.6-slim

WORKDIR /app
COPY . /app

RUN pip install requests locust

ENV HOST http://google.com
ENV NUM 10

CMD locust -f locust.py --host $HOST --no-web -c $NUM -r $NUM
