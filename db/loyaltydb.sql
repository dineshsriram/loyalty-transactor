CREATE TABLE users 
(
	"user_id" 	SERIAL 	     PRIMARY KEY NOT NULL,
	"email" 	VARCHAR(100) UNIQUE 	 NOT NULL,
	"first_name" 	VARCHAR(100) NOT NULL,
	"last_name" 	VARCHAR(100) NOT NULL,
	"points" 	INT    	     NOT NULL,
	"creation_date" TIMESTAMP
);


CREATE TABLE transfers
(
	"transfer_id" 	SERIAL 	     PRIMARY KEY NOT NULL,
	"user_id" 	INT NOT NULL REFERENCES users,
	"points" 	INT NOT NULL,
	"creation_date" TIMESTAMP
);
