""" 
Represents User 
"""

import re

class User:
	"""
	_email=''
	_firstName=''
	_lastName=''
	_points=0
	"""

	def __init__(self, firstName, lastName, email, points=0):
		self._firstName=None
		self._lastName=None
		self._points=None
		self.createUser(firstName, lastName, email, points)

	def createUser(self, firstName, lastName, email, points):
		if self._isValidEmail(email) && self._isValidName(firstName) 
			&& self._isValidName(lastName) && self._isValidPoints(points):
			self._firstName=firstName
			self._lastName=lastName
			self._points=points

	def getUser(self, firstName, lastName, email, points):
		return "user"

	def _isValidEmail(email):
		if email is None:
			return False
		if len(email) > 0:
			if re.match("^.+@([?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$", email) != None:
 				return True
		return False

	def _isValidName(name):
		if name is None:
			return False
		return True if len(name.strip()) > 0 else False

	def _isValidPoints(points):
		if points is None:
			return False
		return True if points >= 0 else False


		
	
