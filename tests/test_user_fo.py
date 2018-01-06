from loyalty_transactor.entities.userFO import UserFO
import pytest

def test_basic():
	me=UserFO("Dinesh", "Sriram", "test@mail.com")
	assert (me.firstName == "Dinesh")
	assert (me.lastName == "Sriram")
	assert (me.email == "test@mail.com" )

def test_bad_email():
	with pytest.raises(RuntimeError):
		UserFO("Dinesh", "Sriram", "testmail.com")
	with pytest.raises(RuntimeError):
		UserFO("Dinesh", "Sriram", "testmailcom")
	with pytest.raises(RuntimeError):
		UserFO("Dinesh", "Sriram", "")
	with pytest.raises(RuntimeError):
		UserFO("Dinesh", "Sriram", "    ")
	with pytest.raises(RuntimeError):
		UserFO("Dinesh", "Sriram", None)

def test_bad_firstname():
	with pytest.raises(RuntimeError):
		UserFO(" ", "Sriram", "test@mail.com")
	with pytest.raises(RuntimeError):
		UserFO("", "Sriram", "test@mail.com")
	with pytest.raises(RuntimeError):
		UserFO(None, "Sriram", "test@mail.com")

def test_bad_lastname():
	with pytest.raises(RuntimeError):
		UserFO("Dinesh", "   ", "test@mail.com")
	with pytest.raises(RuntimeError):
		UserFO("Dinesh", "", "test@mail.com")
	with pytest.raises(RuntimeError):
		UserFO("Dinesh", None, "test@mail.com")




