import os

from locust import task, TaskSequence

load = 10000
MAX_LOAD = 2 ** 24


class UserBehavior(TaskSequence):
    @task
    def index(self):
        self.client.get('/')


class LoadBehavior(TaskSequence):
    @task
    def with_load(self):
        global load
        load = min(MAX_LOAD, load + 250)
        self.client.get(f'/with_load?load={load}')


class WebsiteUser(HttpLocust):
    if os.environ.get('TYPE', 'USER') == 'LOAD':
        task_set = LoadBehavior
    else:
        task_set = UserBehavior
    min_wait = 0
    max_wait = 1000
