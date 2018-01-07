from . import dbService
import json


def createTransfer(transferFO=None):
	if transferFO is None:
		return json.dumps({"error": "Invalid transfer object"})

	# check if users exists
	result=dbService.getUser(transferFO.userId)
	if 'error' in result:
		return json.dumps(result)

	# check if transfer is valid
	user_points=int(result['points'])
	incoming_points=int(transferFO.points)
	if user_points+incoming_points < 0:
		return json.dumps({"error":"User has insufficient funds"})
	# This should be wrapped in a single transaction
	if dbService.createTransfer(transferFO):
		final_points=user_points+incoming_points
		return json.dumps(dbService.updateUser(transferFO.userId, final_points))
	 		
	return json.dumps({"error": "Failed to transfer"})
