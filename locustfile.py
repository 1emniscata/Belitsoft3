from locust import HttpUser, task, between

class WebsiteTestUser(HttpUser):

	@task(1)
	def hello_world(self):
		self.client.get("http://localhost:8000")