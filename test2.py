from locust import HttpUser, task


class HelloWorldUser(HttpUser):
    host = 'https://www.google.com'

    @task
    def hello_world(self):
        self.client.get("")
