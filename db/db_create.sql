CREATE TABLE class
(
        city VARCHAR(25),
        date_created DATETIME DEFAULT NOW(),
	description VARCHAR(200),
        id INTEGER NOT NULL AUTO_INCREMENT,
	price INTEGER,
        PRIMARY KEY (id),
);

CREATE TABLE ticket
(
	class_id INTEGER NOT NULL,
	child_first_name VARCHAR(30),
	child_last_name VARCHAR(30),
	id INTEGER NOT NULL AUTO_INCREMENT,
	user_id INTEGER NOT NULL,
        FOREIGN KEY(user_id) REFERENCES user (id)
        FOREIGN KEY(class_id) REFERENCES class (id)
)

CREATE TABLE user
(       
        first_name VARCHAR(30)
        last_name VARCHAR(30)
        email VARCHAR(50),
        id INTEGER NOT NULL AUTO_INCREMENT,
        password VARCHAR(60),
        PRIMARY KEY (id),
        UNIQUE (email),
);
