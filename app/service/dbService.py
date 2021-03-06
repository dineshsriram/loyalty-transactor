import psycopg2
from datetime import datetime

from ..entities.userFO import UserFO


def connect():
	conn=None
	try:
		conn=psycopg2.connect("postgresql://dinesh:secret@psql:5432/loyaltydb")
#database='loyaltydb', user='dinesh', password='secret', port=5432, host='localhost') 
	except Exception as e:
		print(e)
	return conn 


def getUser(userId=None):
	conn=connect()
	if conn is not None:
		cur=conn.cursor()
		cur.execute("select first_name, last_name, email, points from users where user_id="+str(userId))
		row=cur.fetchone()
		if row is None:
			return {"error": "User Not Found"}

		result = {"firstName":    row[0],
		  	  "lastName" :    row[1],
			  "email" : 	  row[2],
		  	  "points":       row[3]}
		cur.close()
		conn.close()
		return result
	return {"error": "DB Connection Error"}

def getAllUsers():
	conn=connect()
	if conn is not None:
		cur=conn.cursor()
		cur.execute("select user_id, first_name, last_name, email, points from users")
		rows=cur.fetchall()
		if rows is None:
			return {"error": "No Users in System"}

		result=[]
		for row in rows:
			result.append({
			"userId" :   row[0],
			"firstName": row[1],
			"lastName" : row[2],
			"email" :    row[3],
			"points":    row[4]})
		cur.close()
		conn.close()
		return result
	return {"error": "DB Connection Error"}


def updateUser(userId=None, points=None):
	conn=connect()
	if conn is not None:
		cur=conn.cursor()
		cur.execute("update users set points=%s where user_id=%s", (str(points), str(userId)))
		conn.commit()
		cur.close()
		conn.close()
		return getUser(userId)
	return {"error": "DB Connection Error"}


def createUser(userFO=None):
	conn=connect()
	if conn is not None:
		cur=conn.cursor()
		current_time=datetime.now()
		cur.execute("insert into users(first_name,last_name,email,points,creation_date)values(%s, %s, %s, %s, %s)", (userFO.firstName, userFO.lastName, userFO.email, str(0), current_time))
		conn.commit()
		cur.close()
		conn.close()
		return True
	return False


def getAllTransfers(userId=None):
	conn=connect()
	if conn is not None:
		cur=conn.cursor()
		cur.execute("select transfer_id, points from transfers where user_id="+str(userId))
		rows=cur.fetchall()
		if rows is None:
			return {"error": "No Transfers Found"}

		result=[]
		for row in rows:
			result.append({"transfer_id":   row[0],
			       	       "points" :       row[1]})
		cur.close()
		conn.close()
		return result
	return {"error": "DB Connection Error"}


def createTransfer(transferFO=None):
	conn=connect()
	if conn is not None:
		cur=conn.cursor()
		current_time=datetime.now()
		cur.execute("insert into transfers(user_id,points,creation_date)values(%s, %s, %s)", (transferFO.userId, transferFO.points,current_time))
		conn.commit()
		cur.close()
		conn.close()
		return True
	return False

 
