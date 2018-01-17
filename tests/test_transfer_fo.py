from app.entities.transferFO import TransferFO

import pytest

def test_basic():
	me=TransferFO(123, 35)
	assert (me.userId == 123)
	assert (me.points == 35 )

def test_bad_userid():
	with pytest.raises(RuntimeError):
		TransferFO("", 35)
	with pytest.raises(RuntimeError):
		TransferFO(None, 35)


def test_bad_points():
	with pytest.raises(RuntimeError):
		TransferFO(123, "")
	with pytest.raises(RuntimeError):
		TransferFO(123, None)




