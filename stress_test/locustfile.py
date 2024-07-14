import random

from locust import HttpUser, task


class HelloWorldUser(HttpUser):
    @task
    def hello_world(self):
        n = random.randint(1, 10_000)
        self.client.get(f"/factorial?n={n}")
