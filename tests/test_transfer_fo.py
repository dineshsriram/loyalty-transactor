from loyalty_transactor.entities.transferFO import TransferFO,TransferMode

import pytest

def test_basic():
	me=TransferFO(123, TransferMode.ADD_POINTS, 35)
	assert (me.userId == 123)
	assert (me.mode == TransferMode.ADD_POINTS)
	assert (me.points == 35 )

def test_bad_userid():
	with pytest.raises(RuntimeError):
		TransferFO(-123, TransferMode.ADD_POINTS, 35)
	with pytest.raises(RuntimeError):
		TransferFO(None, TransferMode.ADD_POINTS, 35)

def test_bad_mode():
	with pytest.raises(RuntimeError):
		TransferFO(123, -1, 35)
	with pytest.raises(RuntimeError):
		TransferFO(123, 124, 35)

def test_bad_points():
	with pytest.raises(RuntimeError):
		TransferFO(123, TransferMode.DEDUCT_POINTS, -1)
	with pytest.raises(RuntimeError):
		TransferFO(123, TransferMode.ADD_POINTS, -12)




