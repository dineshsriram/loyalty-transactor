"""
Basic Loyalty Transaction System
"""

from flask import Flask,request
import logging
from app.entities.userFO import UserFO
from app.entities.transferFO import TransferFO
from app.service import userService
from app.service import transferService

app=Flask(__name__)

@app.route("/user", methods=['POST'])
def createUser():
	if request.method == 'POST':
		jsonFO=request.get_json()
		userFO=UserFO(jsonFO['firstName'],jsonFO['lastName'],jsonFO['email'])
		return userService.createUser(userFO)


@app.route("/user/<id>", methods=['GET'])
def getUserById(id):
	if request.method == 'GET':
		return userService.getUserById(id)

@app.route("/transfer/<userid>", methods=['GET'])
def getTransfersByUserId(userid):
	if request.method == 'GET':
		return userService.getAllTransfersbyId(userid)

@app.route("/transfer", methods=['PUT'])
def addTransfer():
	if request.method == 'PUT':
		jsonFO=request.get_json()
		transferFO=TransferFO(jsonFO['userId'], jsonFO['points'])
		return transferService.createTransfer(transferFO)


@app.route("/")
def hello():
	return "Basic Loyalty Transaction System"

def main():
	logging.basicConfig(filename="loyalty_transaction.log",
				level=logging.INFO)
	logging.info("Starting REST server")
	app.run(host='0.0.0.0', debug=True)
	logging.info("Closing REST server")

if __name__ == '__main__':
	main()
