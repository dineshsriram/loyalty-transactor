""" 
Represents Transfer Input Object
"""

from enum import Enum

class TransferMode(Enum):
	ADD_POINTS=1
	DEDUCT_POINTS=1

	@classmethod
	def has_value(cls, value):
		return any(value == item for item in cls)


class TransferFO:
	"""
	mode=''
	points=''	
	userId=''
	"""

	def _isValidMode(self, mode):
		if mode:
			return TransferMode.has_value(mode)
		return False
	
	def _isValidPoints(self, points):
		if points:
			return (points >= 0)	
		return False

	def _isValidUserId(self, userId):
		if userId:
			return (userId >= 0)
		return False

	def _validateTransfer(self, userId, mode, points):
		if self._isValidUserId(userId) and self._isValidMode(mode) and self._isValidPoints(points):
			return True
		raise RuntimeError("Invalid Arguments for Transfer")

	def __init__(self, userId=None, mode=None, points=None):
		if self._validateTransfer(userId, mode, points):
			self.userId=userId
			self.mode=mode
			self.points=points

