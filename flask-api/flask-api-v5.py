# demo api using Flask-RESTful and Restless
'''
python flask-api-v5.py
'''
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask.ext.restless import APIManager


app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:abc123@127.0.0.1:5432/mydb'
db = SQLAlchemy(app)


# Model
class Persons(db.Model): # must match the table name for this module
    __tablename__ = 'persons'
#   __table_args__ = {'schema':'<schema_name>'} # for when using schemas
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)


manager = APIManager(app, flask_sqlalchemy_db=db)


manager.create_api(Persons, methods=['GET', 'POST', 'DELETE'])


if __name__ == '__main__':
    app.run()