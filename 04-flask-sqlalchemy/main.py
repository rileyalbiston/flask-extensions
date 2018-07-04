from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
# create database connection
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db' 
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:abc123@127.0.0.1:5432/dev_db' 
db = SQLAlchemy(app)


# create one-to-many relationships 
class Owner(db.Model):
	__tablename__ = 'owner'
#   __table_args__ = {'schema':'<schema_name>'} # for when using schemas
	id = db.Column('id', db.Integer, primary_key=True)
	name = db.Column('name', db.String(100))
	# create the relationship from the parent table to the child talbe. This won't be a column in the database.
	motorcycles = db.relationship('Motorcycle', backref='owner', lazy='dynamic')


	def __repr__(self):
		return self.name


class Motorcycle(db.Model):
	__tablename__ = 'motorcycle'
	#__table_args__ = {'schema':'<schema_name>'} # for when using schemas	id = db.Column('id', db.Integer, primary_key=True)
	id = db.Column('id', db.Integer, primary_key=True)
	make = db.Column('make', db.String(63))
	# foregin key to connect to the Owner table. This will be a column in the table.
	owner_id = db.Column(db.Integer, db.ForeignKey('owner.id'))


	def __repr__(self):
		return f"{self.make, self.owner_id}"

# create many-to-many relationships
#author_book = db.Table('author_book',
#	db.Column('author_id', db.Integer, db.ForeignKey('author.id')),
#	db.Column('book_id', db.Integer, db.ForeignKey('book.id'))
#)
#
#
#class Author(db.Model):
#	id = db.Column('id', db.Integer, primary_key=True)
#	name = db.Column('name', db.String(100))
#	written = db.relationship('Book', secondary=author_book, backref=db.backref('writers', lazy='dynamic'))
#
#
#class Book(db.Model):
#	id = db.Column('id', db.Integer, primary_key=True)
#	title = db.Column('make', db.String(100))


@app.route("/")
def home():
	owner = Owner.query.all()
	return render_template('index.html', data=owner)

@app.route("/motorcycles")
def motorcycles():
	motorcycles = Motorcycle.query.all()
	return render_template('motorcycles.html', data=motorcycles)


if __name__ == '__main__':
	app.run(debug=True, port=5000)


'''
Database Script

-- CREATE DATABASE dev_db;

CREATE TABLE IF NOT EXISTS owner (
	id serial,
	name varchar(63) NOT NULL,
	PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS motorcycle (
	id serial,
	make varchar(63) NOT NULL,
	owner_id int NOT NULL,
	PRIMARY KEY (id)
);

ALTER TABLE motorcycle
ADD CONSTRAINT motorcycle_owner_fkey FOREIGN KEY (owner_id) 
	REFERENCES owner (id) ON UPDATE CASCADE ON DELETE CASCADE;

WITH ins1 AS (
   INSERT INTO owner (name)
   VALUES 
	('John')
   RETURNING id AS dept_id
)
INSERT INTO motorcycle (make, owner_id)
VALUES
	('Honda', (SELECT dept_id FROM ins1));

WITH ins1 AS (
   INSERT INTO owner (name)
   VALUES 
	('Sally')
   RETURNING id AS dept_id
)
INSERT INTO motorcycle (make, owner_id)
VALUES
	('Kawasaki', (SELECT dept_id FROM ins1)),
	('Triumph', (SELECT dept_id FROM ins1));

SELECT * FROM owner;
SELECT * FROM motorcycle;

SELECT o.name AS owner, m.make
FROM owner o INNER JOIN motorcycle m
ON o.id = m.owner_id;
'''
