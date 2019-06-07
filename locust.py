from locust import task, TaskSequence


class UserBehavior(TaskSequence):

    @task
    def index(self):
        self.client.get('/')


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 0
    max_wait = 0
