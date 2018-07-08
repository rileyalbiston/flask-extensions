from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__) 
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:abc123@127.0.0.1:5432/dev_db' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# create many-to-many relationships
author_book = db.Table('author_book',
	db.Column('author_id', db.Integer, db.ForeignKey('author.id'), primary_key=True),
	db.Column('book_id', db.Integer, db.ForeignKey('book.id'), primary_key=True)
)


class Author(db.Model):
	id = db.Column('id', db.Integer, primary_key=True)
	name = db.Column('name', db.String(100))
	wrote = db.relationship('Book', secondary=author_book, backref=db.backref('writers', lazy='dynamic'))


class Book(db.Model):
	id = db.Column('id', db.Integer, primary_key=True)
	title = db.Column('title', db.String(100))


@app.route("/")
def home():
	auth = Author.query.first()
	data = auth.wrote
	return render_template('index.html', auth=auth, data=data)


@app.route("/book")
def book():
	book = Book.query.first()
	data = book.writers
	return render_template('book.html', data=data, book=book)

if __name__ == '__main__':
	app.run(debug=True, port=5000)


'''
Database Script

-- CREATE DATABASE dev_db;

CREATE TABLE IF NOT EXISTS author (
	id serial,
	name varchar(63) NOT NULL,
	PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS book (
	id serial,
	title varchar(63) NOT NULL,
	PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS author_book (
	author_id int NOT NULL,
	book_id int NOT NULL,
	PRIMARY KEY (author_id, book_id)
);

ALTER TABLE author_book
ADD CONSTRAINT author_book_author_fkey FOREIGN KEY (author_id) 
	REFERENCES author (id) ON UPDATE CASCADE ON DELETE CASCADE;

ALTER TABLE author_book
ADD CONSTRAINT author_book_book_fkey FOREIGN KEY (book_id) 
	REFERENCES book (id) ON UPDATE CASCADE ON DELETE CASCADE;


INSERT INTO author (name)
VALUES
	('William Shakespeare'),
	('Leo Tolstoy'),
	('Stephen King');

INSERT INTO book (title)
VALUES
	('Don Quixote'),
	('Moby Dick'),
	('The Odyssey');

INSERT INTO author_book (author_id, book_id)
VALUES
	(1, 1),
	(2, 1),
	(2, 2),
	(2, 3),
	(3, 3),
	(1, 3);

SELECT a.id as auth_id, a.name, b.id as book_id, b.title
FROM  author a
JOIN author_book ab ON a.id = ab.author_id
JOIN book b ON ab.book_id = b.id;
'''
