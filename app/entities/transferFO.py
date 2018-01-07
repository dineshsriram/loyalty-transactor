""" 
Represents Transfer Input Object
"""

class TransferFO:
	"""
	points=''	
	userId=''
	"""

	def _isValidPoints(self, points):
		if points:
			return True
		return False

	def _isValidUserId(self, userId):
		if userId:
			return (userId >= 0)
		return False

	def _validateTransfer(self, userId, points):
		if self._isValidUserId(userId) and self._isValidPoints(points):
			return True
		raise RuntimeError("Invalid Arguments for Transfer")

	def __init__(self, userId=None, points=None):
		if self._validateTransfer(userId, points):
			self.userId=userId
			self.points=points

