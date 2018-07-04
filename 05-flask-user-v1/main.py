# pip install Flask-User<0.7
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_user import login_required, UserManager, UserMixin, SQLAlchemyAdapter


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:abc123@127.0.0.1:5432/dev_db'
app.config['CSRF_ENABLED'] = True
app.config['USER_ENABLE_EMAIL'] = False # change to True later
db = SQLAlchemy(app)

class UserAccount(db.Model, UserMixin):
	__tablename__ = 'user_account'
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(50), nullable=False, unique=True)
	password = db.Column(db.String(255), nullable=False, server_default='')
	active = db.Column(db.Boolean(), nullable=False, server_default='0')


db_adapter = SQLAlchemyAdapter(db, UserAccount)
user_manager = UserManager(db_adapter, app)


@app.route('/')
def index():
	return '<p>Index page</p>'


@app.route('/profile')
@login_required
def profile():
	return '<p>Profile page</p><a href="/user/sign-out">Sign Out</a>'

if __name__ == '__main__':
	app.run(debug=True)

'''
Database Script

-- CREATE DATABASE dev_db;

CREATE TABLE IF NOT EXISTS user_account (
	id serial,
	username varchar(63) NOT NULL,
	password varchar(255) NOT NULL,
	active boolean,
	PRIMARY KEY (id)
);

SELECT * FROM user_account;
'''
