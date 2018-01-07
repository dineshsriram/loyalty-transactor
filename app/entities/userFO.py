""" 
Represents User Input Object
"""

import re

class UserFO:
	"""
	email=''
	firstName=''
	lastName=''
	"""

	def _isValidEmail(self, email):
		if email is None:
			return False
		email=email.strip()
		if len(email) <= 0:
			return False
		if re.match("[^@]+@[^@]+\.[^@]+", email) is None: return False
		return  True

	def _isValidName(self, name):
		if name is None:
			return False
		return True if len(name.strip()) > 0 else False

	def _validateUser(self, firstName, lastName, email):
		if (self._isValidEmail(email) and self._isValidName(firstName) \
			and self._isValidName(lastName)):
			return True
		raise RuntimeError("Invalid Arguments for User")

	def __init__(self, firstName=None, lastName=None, email=None):
		if self._validateUser(firstName, lastName, email):
			self.firstName=firstName
			self.lastName=lastName
			self.email=email

