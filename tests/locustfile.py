from locust import HttpLocust, TaskSet, task
import random
import string
import json

class UserBehavior(TaskSet):
    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        self.createUser()

    def createUser(self):
	def getRandomName(limit=6):
		return ''.join(random.choice(string.ascii_letters) for x in range(limit))
	data={}
	data["firstName"]=getRandomName()
	data["lastName"]=getRandomName()
	data["email"]=data["firstName"]+"."+data["lastName"]+"@test.com"
        self.client.post("/user", json=data)

    @task
    def getAllUsers(self):
        self.client.get("/user")

    @task
    def getUserId(self):
        response=self.client.get("/user/1")
	print("getUserId", response.json())

class User(HttpLocust):
    task_set = UserBehavior
    min_wait = 500
    max_wait = 1000
