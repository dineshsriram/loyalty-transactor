#!/usr/bin/python

"""
Basic Loyalty Transaction System
"""

from flask import Flask
import logging

app=Flask(__name__)

@app.route("/createUser", methods=['POST'])
def createUser():
	return "Created User"

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
