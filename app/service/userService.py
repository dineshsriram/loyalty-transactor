from . import dbService
import json

def createUser(userFO=None):
	if userFO is None:
		return json.dumps({"error": "Invalid user object"})
	if dbService.createUser(userFO):
		return json.dumps(userFO.__dict__)
	return json.dumps({"error": "Failed to create user"})
			

def getUserById(userId=None):
	if userId is None:
		return json.dumps({"error": "Invalid userId"})
	return json.dumps(dbService.getUser(userId))

def getAllUsers():
	return json.dumps(dbService.getAllUsers())

def getAllTransfersbyId(userId=None):	
	if userId is None:
		return json.dumps({"error": "Invalid userId"})
	return json.dumps(dbService.getAllTransfers(userId))
